import React from 'react';
import './App.css';
import DocumentBrowser from './components/DocumentBrowser';
import GlobalSearch from './components/GlobalSearch';
import ConnectionsMap from './components/ConnectionsMap';
import GeoMap from './components/GeoMap';

function App() {
  return (
    <div className="App">
      <h1>Document Browser</h1>
      <GlobalSearch />
      <DocumentBrowser />
      <ConnectionsMap />
      <GeoMap
        locations={[
          {
            name: 'Berlin',
            documents: [
              { id: 1, title: 'Berlin Report' },
              { id: 2, title: 'City History' },
            ],
          },
          {
            name: 'Paris',
            documents: [{ id: 3, title: 'Paris Overview' }],
          },
          {
            name: 'New York',
            documents: [{ id: 4, title: 'NYC Document' }],
          },
        ]}
      />
    </div>
  );
}

export default App;
