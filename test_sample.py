import re
from playwright.sync_api import Playwright, sync_playwright, expect # type: ignore


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context(storage_state="state.json")
    page = context.new_page()
    page.goto("https://www.linkedin.com/jobs")
    # page.wait_for_selector(".text-input")
    # page.locator(".text-input").first.click()
    # page.get_by_role("textbox", name="Email or phone").fill("dhananjay712shukla@gmail.com")
    # page.get_by_role("textbox", name="Password").click()
    # page.get_by_role("textbox", name="Password").fill("")
    # page.get_by_role("button", name="Sign in").click()
    # page.wait_for_selector('[data-test-id="typeahead-input"]')
    page.get_by_test_id("typeahead-input").click()
    page.get_by_test_id("typeahead-input").fill("ai")
    page.get_by_role("link", name="ai engineer jobs · India").click()
    # Find all job cards and print the titles
    page.wait_for_selector(".fd37a291", timeout=10000)
    titles = page.locator(".fd37a291").all_text_contents()
    if len(titles) > 0:
        print(f"✅ Success! Found {len(titles)} jobs:")
    for t in titles:
        print(f"- {t.strip()}")
    else:
        print("❌ No jobs found. Check if the page loaded correctly.")  
    page.wait_for_timeout(5000)    

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
