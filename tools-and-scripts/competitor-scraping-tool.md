layout: default
title: Content Title Generator

# 🕵️‍♂️ Competitor URL Scraping Tool – Static Pages

This Python script crawls through all **internal static pages** of a target website and lists them.  
It’s perfect for **SEO audits**, **competitor research**, or **site mapping**.

---

## 🚀 How It Works
1. **Set Target URL** – Define the competitor’s base URL in the script (`base_url`).
2. **Crawl Internal Pages** – Uses `requests` and `BeautifulSoup` to fetch and parse HTML content.
3. **Extract Links** – Finds `<a>` tags, filters for **internal links only** (same domain).
4. **Avoid Duplicates** – Keeps track of visited and queued pages.
5. **Save Results** – Outputs all discovered URLs and optionally saves them to a `.txt` file.

---

## 📦 Requirements
- Python 3.8+
- `requests`
- `beautifulsoup4`

Install dependencies:
```bash
pip install requests beautifulsoup4
