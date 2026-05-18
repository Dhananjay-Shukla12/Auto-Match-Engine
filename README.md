# Auto Match Engine 

I built the Auto Match Engine over a weekend because manually scrolling through job boards and trying to guess if I actually qualify for a role is exhausting.

I wanted a script that wouldn't just scrape job data, but would actually act as a personal recruiter and tell me: *"Is this job worth applying for based on my exact skills?"*

## What it actually does
1. **The Scraper:** It uses Playwright to grab live AI Engineer job listings from Naukri. (I originally tried LinkedIn and Indeed, but their Cloudflare bot-protection is a nightmare. Naukri was much better for this). 
2. **The Brain:** It extracts the raw job titles and descriptions and feeds them directly into the Google Gemini 1.5 API. 
3. **The Output:** Gemini analyzes the roles against my current resume/skills and prints out a customized recommendation in the terminal telling me which job is the best fit.

## Tech Stack
- **Python** (Core logic)
- **Playwright** (Headless browser automation & DOM parsing)
- **Google Gemini API** (LLM analysis)

## How to run it locally

If you hate scrolling through job boards too, feel free to clone this and use it.
