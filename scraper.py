import re
from playwright.sync_api import Playwright, sync_playwright, expect # type: ignore

def all_data():
    jobs_data = []
    def run(playwright: Playwright) -> None:
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context(storage_state="naukri.json")
        page = context.new_page()
        page.wait_for_timeout(3000)
        page.goto("https://www.naukri.com/mnjuser/homepage")
        page.wait_for_timeout(3000)
        page.get_by_text("Search jobs here").click()
        page.get_by_role("textbox", name="Enter keyword / designation").fill("AI")
        page.get_by_role("textbox", name="Select experience").click()
        page.locator("div").filter(has_text=re.compile(r"^3 years$")).click()
        page.get_by_role("button", name=" Search").click()
        page.locator("label").filter(has_text="Work from office").locator("i").wait_for()
        page.locator("label").filter(has_text="Work from office").locator("i").click()
        page.locator("label").filter(has_text="Remote").locator("i").wait_for()
        page.locator("label").filter(has_text="Remote").locator("i").click()
        page.locator("label").filter(has_text="Hybrid").locator("i").wait_for()
        page.locator("label").filter(has_text="Hybrid").locator("i").click()
        page.locator("label").filter(has_text="Engineering - Soft").locator("i").wait_for()
        page.locator("label").filter(has_text="Engineering - Soft").locator("i").click()
        page.locator("label").filter(has_text="Data Science & An").locator("i").wait_for()
        page.locator("label").filter(has_text="Data Science & An").locator("i").click()
        page.mouse.wheel(0, 300)
        page.locator("label").filter(has_text="10-15 Lakhs").locator("i").wait_for()
        page.locator("label").filter(has_text="10-15 Lakhs").locator("i").click()
        page.locator("label").filter(has_text="15-25 Lakhs").locator("i").wait_for()
        page.locator("label").filter(has_text="15-25 Lakhs").locator("i").click()
        page.locator("label").filter(has_text="25-50 Lakhs").locator("i").wait_for()
        page.locator("label").filter(has_text="25-50 Lakhs").locator("i").click()
        page.locator("label").filter(has_text="50-75 Lakhs").locator("i").wait_for()
        page.locator("label").filter(has_text="50-75 Lakhs").locator("i").click()
        
        jobs = page.locator("h2 a.title")
        count = jobs.count()
        print("Total jobs:", count)
        
        for i in range(min(5, count)):

                job = jobs.nth(i)

                
                title = job.inner_text()
                job.click()
                page.wait_for_timeout(3000)
                new_tab = page.context.pages[-1]
                new_tab.mouse.wheel(0, 300)
                new_tab.locator("h2:has-text('Job description')").wait_for()
                description = new_tab.locator(".styles_JDC__dang-inner-html__h0K4t").inner_text()

                new_tab.mouse.wheel(0, 300)

                jobs_data.append((title,description[:1000]))
                new_tab.close()
    
    
    # ---------------------
        context.close()
        browser.close()


    with sync_playwright() as playwright:
        run(playwright)
    
    return jobs_data

    