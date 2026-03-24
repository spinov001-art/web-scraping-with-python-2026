# Web Scraping with Python 2026 — Complete Guide

Everything you need to scrape the web with Python in 2026. From `requests` to Playwright, from simple APIs to anti-bot bypass.

## The Decision Tree

```
Need data from a website?
│
├── Has an API? → Use the API (fastest, most reliable)
│   └── [200+ Free APIs List](https://github.com/Spinov001-art/free-apis-list)
│
├── Static HTML? → requests + BeautifulSoup
│
├── JavaScript-rendered? → Playwright
│   └── [Selenium vs Playwright](https://github.com/Spinov001-art/selenium-vs-playwright-2026)
│
├── Anti-bot protection? → Playwright + proxies
│   └── [Proxies Guide](https://github.com/Spinov001-art/web-scraping-proxies-guide)
│
└── Rate limited? → Add backoff + circuit breaker
    └── [Error Handling](https://github.com/Spinov001-art/web-scraping-error-handling)
```

## Quick Start Examples

### 1. Simple HTTP Request

```python
import requests

r = requests.get("https://api.github.com/repos/torvalds/linux")
data = r.json()
print(f"Linux: {data['stargazers_count']:,} stars")
```

### 2. Parse HTML with BeautifulSoup

```python
import requests
from bs4 import BeautifulSoup

r = requests.get("https://news.ycombinator.com")
soup = BeautifulSoup(r.text, "html.parser")

for item in soup.select(".titleline > a")[:5]:
    print(item.text)
```

### 3. JavaScript-Rendered Pages (Playwright)

```python
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()
    page.goto("https://example.com")
    
    # Wait for dynamic content
    page.wait_for_selector(".results")
    content = page.content()
    
    browser.close()
```

### 4. API-First Approach (Best Practice)

```python
import requests

# Instead of scraping Google, use SerpAPI or similar
# Instead of scraping Twitter, use the API
# Instead of scraping YouTube, use Innertube API

# Example: Hacker News API (no scraping needed)
r = requests.get("https://hacker-news.firebaseio.com/v0/topstories.json")
top_ids = r.json()[:5]

for story_id in top_ids:
    story = requests.get(f"https://hacker-news.firebaseio.com/v0/item/{story_id}.json").json()
    print(f"  {story['score']} pts | {story['title']}")
```

## Essential Libraries

| Library | Purpose | Install |
|---------|---------|---------|
| `requests` | HTTP requests | `pip install requests` |
| `beautifulsoup4` | HTML parsing | `pip install beautifulsoup4` |
| `playwright` | Browser automation | `pip install playwright && playwright install` |
| `lxml` | Fast XML/HTML parser | `pip install lxml` |
| `httpx` | Async HTTP | `pip install httpx` |
| `parsel` | CSS/XPath selectors | `pip install parsel` |
| `scrapy` | Full framework | `pip install scrapy` |

## Production Patterns

| Pattern | Guide |
|---------|-------|
| Error handling | [Retry, circuit breaker, DLQ](https://github.com/Spinov001-art/web-scraping-error-handling) |
| Rate limiting | [50+ API limits](https://github.com/Spinov001-art/api-rate-limits-guide) |
| Authentication | [OAuth, API keys, JWT](https://github.com/Spinov001-art/api-authentication-guide) |
| Proxy rotation | [Free and paid options](https://github.com/Spinov001-art/web-scraping-proxies-guide) |
| Browser choice | [Selenium vs Playwright](https://github.com/Spinov001-art/selenium-vs-playwright-2026) |

## Ethical Scraping Checklist

- [ ] Check robots.txt before scraping
- [ ] Respect rate limits (add delays between requests)
- [ ] Set a descriptive User-Agent header
- [ ] Don't scrape personal data without consent
- [ ] Use APIs when available (they exist more often than you think)
- [ ] Cache responses to avoid repeated requests
- [ ] Follow the site's Terms of Service

## The Complete Ecosystem

All our web scraping tools and guides:

- [Awesome Web Scraping 2026](https://github.com/Spinov001-art/awesome-web-scraping-2026) ⭐9 — 500+ tools
- [Free APIs List](https://github.com/Spinov001-art/free-apis-list) — 200+ no-auth APIs
- [AI Market Research Reports](https://github.com/Spinov001-art/ai-market-research-reports) — 500+ reports
- [Python Data Pipelines](https://github.com/Spinov001-art/python-data-pipelines) — 15 templates

## License

MIT
