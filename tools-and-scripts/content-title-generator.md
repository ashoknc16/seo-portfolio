---
layout: default
title: Content Title Generator
---

# 📝 Content Title Generator

This Python script automates the process of generating **SEO-friendly content titles** based on keyword research data.  
It fetches **real Google Autocomplete suggestions** via SerpAPI and uses **OpenAI GPT** to create trending, click-worthy blog post titles tailored to UK audiences.

---

## 🚀 How It Works
1. **Enter a Keyword** – The script starts with a single keyword (e.g. `"Any keyword"`).
2. **Fetch Suggestions** – It queries SerpAPI to pull related keyword suggestions from Google Autocomplete.
3. **Analyse Search Intent** – The keyword list is passed to OpenAI GPT.
4. **Generate Titles** – GPT outputs **three unique blog update ideas** and **one non-generic headline**, focusing on current trends, legal updates, and UK-specific context.
5. **Automate Content** - Automates content based on the Title and generates a 1200 word article.

---

## 📦 Requirements
- Python 3.8+
- [SerpAPI Account & API Key](https://serpapi.com/)
- [OpenAI API Key](https://platform.openai.com/)

Install dependencies:
```bash
pip install serpapi openai
