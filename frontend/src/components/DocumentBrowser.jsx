import React, { useState } from 'react';
import DocumentViewer from './DocumentViewer';
import './DocumentBrowser.css';

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
    <div className="browser-container">
      <div className="toolbar">
        <button onClick={() => window.open('/export?format=pdf')}>Export PDF</button>
        <button onClick={() => window.open('/export?format=csv')}>Export CSV</button>
      </div>

      <div className="filters">
        <label>
          Type:
          <select name="type" value={filters.type} onChange={handleFilterChange}>
            <option value="">All</option>
            <option value="pdf">PDF</option>
            <option value="html">HTML</option>
            <option value="image">Image</option>
          </select>
        </label>
        <label>
          Topic:
          <input
            type="text"
            name="topic"
            value={filters.topic}
            onChange={handleFilterChange}
            placeholder="Topic"
          />
        </label>
        <label>
          Date:
          <input
            type="date"
            name="date"
            value={filters.date}
            onChange={handleFilterChange}
          />
        </label>
      </div>

      <div className="view-toggle">
        <button
          className={view === 'list' ? 'active' : ''}
          onClick={() => setView('list')}
        >
          List
        </button>
        <button
          className={view === 'grid' ? 'active' : ''}
          onClick={() => setView('grid')}
        >
          Grid
        </button>
      </div>

      <div className={`docs ${view === 'grid' ? 'grid' : ''}`}>
        {filteredDocs.map((doc) => (
          <div
            key={doc.id}
            onClick={() => setSelected(doc)}
            className="doc-card"
          >
            <strong className="doc-title">{doc.title}</strong>
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
