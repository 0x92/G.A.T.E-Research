import React from 'react';
import NoteEditor from './NoteEditor';

function DocumentViewer({ document, onClose }) {
  if (!document) return null;

  let content;
  switch (document.type) {
    case 'image':
      content = (
        <img
          src={document.url}
          alt={document.title}
          style={{ maxWidth: '100%', maxHeight: '80vh' }}
        />
      );
      break;
    case 'pdf':
      content = (
        <iframe
          src={document.url}
          title={document.title}
          style={{ width: '100%', height: '80vh' }}
        />
      );
      break;
    case 'html':
    default:
      content = (
        <iframe
          src={document.url}
          title={document.title}
          style={{ width: '100%', height: '80vh' }}
        />
      );
  }

  return (
    <div style={{ marginTop: '1rem' }}>
      <button onClick={onClose} style={{ marginBottom: '0.5rem' }}>
        Close
      </button>
      {content}
      <NoteEditor docId={document.id} />
    </div>
  );
}

export default DocumentViewer;
