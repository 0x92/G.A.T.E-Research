import React, { useEffect, useState } from 'react';

function NoteEditor({ docId }) {
  const [text, setText] = useState('');
  const [tags, setTags] = useState('');

  useEffect(() => {
    if (!docId) return;
    fetch(`/notes/${docId}`)
      .then((res) => res.json())
      .then((data) => {
        setText(data.text || '');
        setTags((data.tags || []).join(', '));
      });
  }, [docId]);

  const save = () => {
    fetch(`/notes/${docId}`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        text,
        tags: tags
          .split(',')
          .map((t) => t.trim())
          .filter((t) => t.length > 0)
      })
    });
  };

  return (
    <div style={{ marginTop: '1rem' }}>
      <textarea
        value={text}
        onChange={(e) => setText(e.target.value)}
        rows={5}
        style={{ width: '100%' }}
        placeholder="Write notes here..."
      />
      <input
        value={tags}
        onChange={(e) => setTags(e.target.value)}
        placeholder="Tags (comma separated)"
        style={{ width: '100%', marginTop: '0.5rem' }}
      />
      <button onClick={save} style={{ marginTop: '0.5rem' }}>
        Save
      </button>
    </div>
  );
}

export default NoteEditor;
