from playwright.sync_api import sync_playwright # type: ignore

with sync_playwright() as p:
    browser = p.chromium.launch(
        headless=False
    )  # Set headless=True if you don't want to see the browser
    page = browser.new_page()
    page.goto("https://www.google.com")
    print("Page title:", page.title())
    browser.close()