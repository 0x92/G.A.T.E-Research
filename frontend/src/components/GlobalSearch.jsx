import React, { useEffect, useState } from 'react';

function GlobalSearch() {
  const [query, setQuery] = useState('');
  const [results, setResults] = useState([]);

  useEffect(() => {
    if (!query) {
      setResults([]);
      return;
    }

    const controller = new AbortController();

    const timeout = setTimeout(async () => {
      try {
        const res = await fetch(`/search?q=${encodeURIComponent(query)}`, {
          signal: controller.signal
        });
        if (!res.ok) return;
        const data = await res.json();
        setResults(data.hits || []);
      } catch (err) {
        if (err.name !== 'AbortError') console.error(err);
      }
    }, 300);

    return () => {
      clearTimeout(timeout);
      controller.abort();
    };
  }, [query]);

  return (
    <div>
      <input
        type="text"
        value={query}
        placeholder="Search..."
        onChange={(e) => setQuery(e.target.value)}
        autoComplete="off"
      />
      {results.length > 0 && (
        <ul>
            {results.map((hit) => {
              const snippet =
                (hit._formatted &&
                  (hit._formatted.content ||
                    hit._formatted.text ||
                    hit._formatted.ocrText ||
                    '')) ||
                '';
              return (
              <li key={hit.id} style={{ marginBottom: '1rem' }}>
                <strong>{hit.title || hit.id}</strong>
                {snippet && (
                  <div
                    style={{ fontSize: '0.9rem' }}
                    dangerouslySetInnerHTML={{ __html: snippet }}
                  />
                )}
                {hit.source && <div>Source: {hit.source}</div>}
                {hit.topics && hit.topics.length > 0 && (
                  <div>Topics: {hit.topics.join(', ')}</div>
                )}
                {hit.entities && hit.entities.length > 0 && (
                  <div>Entities: {hit.entities.join(', ')}</div>
                )}
              </li>
            );
          })}
        </ul>
      )}
    </div>
  );
}

export default GlobalSearch;

