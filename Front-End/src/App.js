import React, { useState } from "react";
import axios from "axios";
import "./App.css"; // Import styles

const App = () => {
  const [query, setQuery] = useState("");
  const [results, setResults] = useState([]);
  const [aiSearch, setAiSearch] = useState(false);
  const [sortBy, setSortBy] = useState("relevance");
  const [searched, setSearched] = useState(false);

  const handleSearch = async () => {
    if (!query.trim()) {
      alert("Please enter a search query.");
      return;
    }

    if (aiSearch) {
      alert("⚠️ AI search is enabled. Results may not always be accurate. Use discretion.");
    }

    try {
      const response = await axios.get("http://127.0.0.1:8000/search", {
        params: { query, ai_search: aiSearch, sort_by: sortBy },
      });

      setResults(response.data.results);
      setSearched(true);
    } catch (error) {
      console.error("Search failed:", error);
    }
  };

  return (
    <div className={`container ${searched ? "after-search" : ""}`}>
      {/* Top search bar (After search) */}
      {searched && (
        <div className="top-bar">
          <input
            type="text"
            className="search-box small"
            value={query}
            onChange={(e) => setQuery(e.target.value)}
          />
          <button className="search-button" onClick={handleSearch}>
            Search
          </button>
        </div>
      )}

      {/* Centered Search (Before Search) */}
      {!searched && (
        <div className="center-search">
          <h1>AI Search Tool</h1>
          <input
            type="text"
            className="search-box large"
            placeholder="Enter search query..."
            value={query}
            onChange={(e) => setQuery(e.target.value)}
          />
          <button className="search-button" onClick={handleSearch}>
            Search
          </button>

          {/* Toggle AI Search */}
          <label className="toggle">
            <input type="checkbox" checked={aiSearch} onChange={() => setAiSearch(!aiSearch)} />
            Enable AI Search
          </label>

          {/* Sorting Options */}
          <select value={sortBy} onChange={(e) => setSortBy(e.target.value)}>
            <option value="relevance">Sort by Relevance</option>
            <option value="date">Sort by Date</option>
            <option value="source">Sort by Source</option>
          </select>
        </div>
      )}

      {/* Query Display (Google Style) */}
      {searched && <p className="query-display">Showing results for: <strong>{query}</strong></p>}

      {/* Results Section */}
      {searched && (
        <div className="results-container">
          <div className="results-section google">
            <h3>🔍 Google Results</h3>
            {results
              .filter((result) => result.source === "Google")
              .map((result, index) => (
                <div key={index} className="result-card">
                  <h4>{result.title}</h4>
                  <p>{result.snippet}</p>
                  <a href={result.link} target="_blank" rel="noopener noreferrer">
                    View More
                  </a>
                </div>
              ))}
          </div>

          <div className="results-section youtube">
            <h3>📺 YouTube Results</h3>
            {results
              .filter((result) => result.source === "YouTube")
              .map((result, index) => (
                <div key={index} className="result-card">
                  <h4>{result.title}</h4>
                  <p>{result.snippet}</p>
                  <a href={result.link} target="_blank" rel="noopener noreferrer">
                    Watch Video
                  </a>
                </div>
              ))}
          </div>
        </div>
      )}
    </div>
  );
};

export default App;
