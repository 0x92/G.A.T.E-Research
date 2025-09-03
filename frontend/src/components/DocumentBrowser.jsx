import React, { useState } from 'react';
import DocumentViewer from './DocumentViewer';

const documents = [
  {
    id: 1,
    title: 'Example PDF',
    type: 'pdf',
    topic: 'Research',
    date: '2023-10-01',
    url: 'https://www.w3.org/WAI/ER/tests/xhtml/testfiles/resources/pdf/dummy.pdf'
  },
  {
    id: 2,
    title: 'Example HTML',
    type: 'html',
    topic: 'Guidelines',
    date: '2023-09-15',
    url: '/sample.html'
  },
  {
    id: 3,
    title: 'Example Image',
    type: 'image',
    topic: 'Design',
    date: '2023-11-20',
    url: 'https://via.placeholder.com/300'
  }
];

function DocumentBrowser() {
  const [view, setView] = useState('list');
  const [filters, setFilters] = useState({ type: '', topic: '', date: '' });
  const [selected, setSelected] = useState(null);

  const handleFilterChange = (e) => {
    const { name, value } = e.target;
    setFilters((prev) => ({ ...prev, [name]: value }));
  };

  const filteredDocs = documents.filter((doc) => {
    return (
      (!filters.type || doc.type === filters.type) &&
      (!filters.topic || doc.topic.toLowerCase().includes(filters.topic.toLowerCase())) &&
      (!filters.date || doc.date === filters.date)
    );
  });

  return (
    <div>
      <div style={{ marginBottom: '1rem' }}>
        <label>
          Type:
          <select name="type" value={filters.type} onChange={handleFilterChange}>
            <option value="">All</option>
            <option value="pdf">PDF</option>
            <option value="html">HTML</option>
            <option value="image">Image</option>
          </select>
        </label>
        <label style={{ marginLeft: '1rem' }}>
          Topic:
          <input
            type="text"
            name="topic"
            value={filters.topic}
            onChange={handleFilterChange}
            placeholder="Topic"
          />
        </label>
        <label style={{ marginLeft: '1rem' }}>
          Date:
          <input
            type="date"
            name="date"
            value={filters.date}
            onChange={handleFilterChange}
          />
        </label>
      </div>

      <div style={{ marginBottom: '1rem' }}>
        <button onClick={() => setView('list')}>List</button>
        <button onClick={() => setView('grid')} style={{ marginLeft: '0.5rem' }}>
          Grid
        </button>
      </div>

      <div
        style={
          view === 'grid'
            ? {
                display: 'grid',
                gridTemplateColumns: 'repeat(auto-fill, minmax(150px, 1fr))',
                gap: '1rem'
              }
            : {}
        }
      >
        {filteredDocs.map((doc) => (
          <div
            key={doc.id}
            onClick={() => setSelected(doc)}
            style={{
              border: '1px solid #ccc',
              padding: '0.5rem',
              cursor: 'pointer'
            }}
          >
            <strong>{doc.title}</strong>
            <div>{doc.type.toUpperCase()}</div>
            <div>{doc.topic}</div>
            <div>{doc.date}</div>
          </div>
        ))}
      </div>

      {selected && (
        <DocumentViewer document={selected} onClose={() => setSelected(null)} />
      )}
    </div>
  );
}

export default DocumentBrowser;
