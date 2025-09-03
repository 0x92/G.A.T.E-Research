import React from 'react';
import './App.css';
import DocumentBrowser from './components/DocumentBrowser';
import GlobalSearch from './components/GlobalSearch';
import ConnectionsMap from './components/ConnectionsMap';

function App() {
  return (
    <div className="App">
      <h1>Document Browser</h1>
      <GlobalSearch />
      <DocumentBrowser />
      <ConnectionsMap />
    </div>
  );
}

export default App;
