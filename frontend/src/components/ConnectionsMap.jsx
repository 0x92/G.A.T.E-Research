import React, { useEffect, useRef, useState } from 'react';
import cytoscape from 'cytoscape';

function ConnectionsMap() {
  const containerRef = useRef(null);
  const [selected, setSelected] = useState(null);

  useEffect(() => {
    if (!containerRef.current) return;

    const cy = cytoscape({
      container: containerRef.current,
      elements: [
        // Nodes
        {
          data: {
            id: 'person1',
            label: 'Alice',
            type: 'person',
            metadata: { role: 'Researcher' }
          }
        },
        {
          data: {
            id: 'org1',
            label: 'Acme Corp',
            type: 'organization',
            metadata: { location: 'NYC' }
          }
        },
        {
          data: {
            id: 'doc1',
            label: 'Doc A',
            type: 'document',
            metadata: {
              url: 'https://example.com/doc-a',
              title: 'Doc A'
            }
          }
        },
        {
          data: {
            id: 'doc2',
            label: 'Doc B',
            type: 'document',
            metadata: {
              url: 'https://example.com/doc-b',
              title: 'Doc B'
            }
          }
        },
        // Edges
        {
          data: {
            id: 'p1d1',
            source: 'person1',
            target: 'doc1',
            label: 'erwähnt in'
          }
        },
        {
          data: {
            id: 'o1d1',
            source: 'org1',
            target: 'doc1',
            label: 'erwähnt in'
          }
        },
        {
          data: {
            id: 'd1d2',
            source: 'doc1',
            target: 'doc2',
            label: 'verlinkt mit',
            type: 'link'
          }
        }
      ],
      style: [
        {
          selector: 'node',
          style: {
            label: 'data(label)',
            'text-valign': 'center',
            'text-halign': 'center',
            color: '#fff'
          }
        },
        {
          selector: 'node[type="person"]',
          style: { 'background-color': '#3498db' }
        },
        {
          selector: 'node[type="organization"]',
          style: { 'background-color': '#2ecc71' }
        },
        {
          selector: 'node[type="document"]',
          style: { 'background-color': '#e67e22' }
        },
        {
          selector: 'edge',
          style: {
            label: 'data(label)',
            'curve-style': 'bezier',
            'target-arrow-shape': 'triangle',
            'line-color': '#ccc',
            'target-arrow-color': '#ccc',
            'font-size': 10
          }
        },
        {
          selector: 'edge[type="link"]',
          style: { 'line-style': 'dashed' }
        }
      ],
      layout: { name: 'grid' }
    });

    cy.on('tap', 'node', (evt) => {
      const data = evt.target.data();
      setSelected(data);
    });

    return () => cy.destroy();
  }, []);

  return (
    <div>
      <div
        ref={containerRef}
        style={{ width: '600px', height: '400px', border: '1px solid #ccc' }}
      />
      {selected && (
        <div style={{ marginTop: '1rem' }}>
          <h3>{selected.label}</h3>
          {selected.metadata && (
            <div>
              {Object.entries(selected.metadata).map(([key, value]) => (
                <div key={key}>
                  <strong>{key}:</strong>{' '}
                  {key === 'url' ? (
                    <a href={value} target="_blank" rel="noreferrer">
                      {value}
                    </a>
                  ) : (
                    value
                  )}
                </div>
              ))}
            </div>
          )}
        </div>
      )}
    </div>
  );
}

export default ConnectionsMap;
