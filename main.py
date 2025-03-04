import os
import asyncio
from dotenv import load_dotenv
from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from serpapi import GoogleSearch
from transformers import pipeline
from googleapiclient.discovery import build
from concurrent.futures import ThreadPoolExecutor
from typing import Optional, List

# Load environment variables
load_dotenv()
SERPAPI_KEY = os.getenv("SERPAPI_KEY")
YOUTUBE_API_KEY = os.getenv("YOUTUBE_API_KEY")

app = FastAPI()

# Enable CORS for frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load AI query expansion model
query_expansion = pipeline("text2text-generation", model="facebook/bart-large-cnn")

# Thread pool for concurrency
executor = ThreadPoolExecutor(max_workers=2)

@app.get("/search")
async def search(
    query: str = Query(..., min_length=1, max_length=200),
    ai_search: bool = Query(False),
    sort_by: Optional[str] = Query("relevance", enum=["relevance", "date", "source"])
):
    expanded_query = await expand_query(query) if ai_search else query

    # Run Google & YouTube searches in parallel
    loop = asyncio.get_event_loop()
    google_task = loop.run_in_executor(executor, fetch_google_results, expanded_query)
    youtube_task = loop.run_in_executor(executor, fetch_youtube_results, expanded_query)

    google_results, youtube_results = await asyncio.gather(google_task, youtube_task)

    all_results = google_results + youtube_results
    ranked_results = rank_results(all_results, sort_by)

    return {
        "original_query": query,
        "expanded_query": expanded_query if ai_search else None,
        "sorted_by": sort_by,
        "results": ranked_results
    }

async def expand_query(query: str):
    try:
        expansion = query_expansion(f"Expand: {query}", max_length=32, num_return_sequences=1)
        return expansion[0]["generated_text"]
    except Exception:
        return query  # Return original query if expansion fails

def fetch_google_results(query: str):
    try:
        search = GoogleSearch({"q": query, "api_key": SERPAPI_KEY})
        results = search.get_dict()
        return [{"title": item.get("title", "No Title"), "link": item.get("link", "#"), "snippet": item.get("snippet", ""), "source": "Google"} for item in results.get("organic_results", [])[:5]]
    except Exception:
        return []

def fetch_youtube_results(query: str):
    try:
        youtube = build("youtube", "v3", developerKey=YOUTUBE_API_KEY)
        request = youtube.search().list(q=query, part="snippet", type="video", maxResults=5, order="relevance")
        response = request.execute()
        return [{"title": item["snippet"]["title"], "link": f"https://www.youtube.com/watch?v={item['id']['videoId']}", "snippet": item["snippet"].get("description", ""), "source": "YouTube"} for item in response.get("items", []) if "videoId" in item["id"]]
    except Exception:
        return []

def rank_results(results: List[dict], sort_by: str):
    if sort_by == "date":
        return sorted(results, key=lambda x: x.get("date", ""), reverse=True)
    elif sort_by == "source":
        return sorted(results, key=lambda x: x["source"])
    return results  # Default sorting
