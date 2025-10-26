# scraper.py
import requests
from bs4 import BeautifulSoup
import re

def scrape_wikipedia(url: str):
    """Fetch and clean Wikipedia article content."""
    response = requests.get(url)
    if response.status_code != 200:
        raise Exception(f"Failed to fetch page: {url}")

    soup = BeautifulSoup(response.text, "html.parser")

    # Extract title
    title = soup.find("h1", {"id": "firstHeading"}).text.strip()

    # Extract main content
    content_div = soup.find("div", {"id": "mw-content-text"})
    if not content_div:
        raise Exception("Main content not found")

    # Remove unwanted tags (references, tables, etc.)
    for tag in content_div.find_all(["sup", "table", "span", "style", "script"]):
        tag.decompose()

    text = content_div.get_text(separator="\n", strip=True)
    text = re.sub(r'\[[0-9]+\]', '', text)  # Remove reference numbers like [1], [2]
    clean_text = ' '.join(text.split())

    return {"title": title, "content": clean_text}
