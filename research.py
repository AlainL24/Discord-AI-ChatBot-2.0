from duckduckgo_search import DDGS
from filters import is_valid_source

MAX_RESULTS = 25


def search_sources(query):

    sources = []

    with DDGS() as ddgs:

        results = ddgs.text(
            query,
            max_results=MAX_RESULTS
        )

        for r in results:

            title = r.get("title")
            url = r.get("href")

            if not title or not url:
                continue

            if not is_valid_source(title, url):
                continue

            sources.append({
                "title": title,
                "url": url
            })

    return sources[:12]