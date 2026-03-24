"""
Quick Scrape — one-file web scraper for common tasks.
Copy-paste ready. No framework needed.

Usage:
    python quick_scrape.py
"""

import requests
from bs4 import BeautifulSoup
import json
import csv
import time


def scrape_links(url: str) -> list[dict]:
    """Extract all links from a page."""
    r = requests.get(url, headers={"User-Agent": "QuickScrape/1.0"}, timeout=10)
    soup = BeautifulSoup(r.text, "html.parser")
    links = []
    for a in soup.find_all("a", href=True):
        links.append({"text": a.get_text(strip=True), "href": a["href"]})
    return links


def scrape_headings(url: str) -> list[dict]:
    """Extract all headings (h1-h6) from a page."""
    r = requests.get(url, headers={"User-Agent": "QuickScrape/1.0"}, timeout=10)
    soup = BeautifulSoup(r.text, "html.parser")
    headings = []
    for tag in ["h1", "h2", "h3", "h4", "h5", "h6"]:
        for h in soup.find_all(tag):
            headings.append({"level": tag, "text": h.get_text(strip=True)})
    return headings


def scrape_meta(url: str) -> dict:
    """Extract meta information from a page."""
    r = requests.get(url, headers={"User-Agent": "QuickScrape/1.0"}, timeout=10)
    soup = BeautifulSoup(r.text, "html.parser")
    meta = {"url": url, "title": soup.title.string if soup.title else None}
    for tag in soup.find_all("meta"):
        name = tag.get("name") or tag.get("property", "")
        content = tag.get("content", "")
        if name and content:
            meta[name] = content
    return meta


def save_json(data, filename="output.json"):
    with open(filename, "w") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    print(f"Saved {len(data) if isinstance(data, list) else 1} items to {filename}")


def save_csv(data: list[dict], filename="output.csv"):
    if not data:
        return
    with open(filename, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=data[0].keys())
        writer.writeheader()
        writer.writerows(data)
    print(f"Saved {len(data)} rows to {filename}")


if __name__ == "__main__":
    url = "https://news.ycombinator.com"
    
    print(f"Scraping: {url}\n")
    
    # Meta info
    meta = scrape_meta(url)
    print(f"Title: {meta.get('title')}")
    
    # Headings
    headings = scrape_headings(url)
    print(f"\nHeadings ({len(headings)}):")
    for h in headings[:5]:
        print(f"  <{h['level']}> {h['text'][:60]}")
    
    # Links
    links = scrape_links(url)
    print(f"\nLinks ({len(links)}):")
    for link in links[:5]:
        print(f"  {link['text'][:40]:40s} → {link['href'][:50]}")
    
    # Save
    save_json(links, "hn_links.json")
    save_csv(links, "hn_links.csv")
    
    print("\nDone! Check hn_links.json and hn_links.csv")
