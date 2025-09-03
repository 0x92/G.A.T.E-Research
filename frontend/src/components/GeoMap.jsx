import React, { useEffect, useState } from 'react';
import { MapContainer, TileLayer, Marker, Popup, useMap } from 'react-leaflet';
import 'leaflet/dist/leaflet.css';
import L from 'leaflet';
import 'leaflet.heat';

// Fix default icon paths for Leaflet when used with bundlers
import markerIcon from 'leaflet/dist/images/marker-icon.png';
import markerShadow from 'leaflet/dist/images/marker-shadow.png';

L.Icon.Default.mergeOptions({
  iconUrl: markerIcon,
  shadowUrl: markerShadow,
});

function HeatLayer({ points }) {
  const map = useMap();
  useEffect(() => {
    if (!points || !points.length) return;
    const layer = L.heatLayer(points, { radius: 25 });
    layer.addTo(map);
    return () => {
      layer.remove();
    };
  }, [map, points]);
  return null;
}

/**
 * GeoMap component
 * @param {{locations: Array<{ name: string, documents: Array<{id:string|number,title:string}> }>}} props
 */
function GeoMap({ locations }) {
  const [places, setPlaces] = useState([]); // [{name, documents, lat, lon}]
  const [heatMode, setHeatMode] = useState(false);

  useEffect(() => {
    async function geocode() {
      const results = await Promise.all(
        locations.map(async (loc) => {
          const url = `https://nominatim.openstreetmap.org/search?format=json&q=${encodeURIComponent(
            loc.name,
          )}`;
          try {
            const res = await fetch(url);
            const data = await res.json();
            if (data && data.length) {
              return {
                ...loc,
                lat: parseFloat(data[0].lat),
                lon: parseFloat(data[0].lon),
              };
            }
          } catch (err) {
            console.error('Geocoding error', err);
          }
          return null;
        }),
      );
      setPlaces(results.filter(Boolean));
    }

    geocode();
  }, [locations]);

  const center = places.length
    ? [places[0].lat, places[0].lon]
    : [51.1657, 10.4515]; // Default: Germany

  const heatPoints = places.map((p) => [p.lat, p.lon, p.documents.length]);

  return (
    <div>
      <button type="button" onClick={() => setHeatMode((m) => !m)}>
        {heatMode ? 'Show Markers' : 'Show Heatmap'}
      </button>
      <MapContainer center={center} zoom={4} style={{ height: '400px', width: '100%' }}>
        <TileLayer
          url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
          attribution="&copy; OpenStreetMap contributors"
        />
        {heatMode && <HeatLayer points={heatPoints} />}
        {!heatMode &&
          places.map((p) => (
            <Marker key={p.name} position={[p.lat, p.lon]}>
              <Popup>
                <strong>{p.name}</strong>
                <ul>
                  {p.documents.map((d) => (
                    <li key={d.id}>{d.title}</li>
                  ))}
                </ul>
              </Popup>
            </Marker>
          ))}
      </MapContainer>
    </div>
  );
}

export default GeoMap;

