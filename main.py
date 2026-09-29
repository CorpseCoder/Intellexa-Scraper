from playwright.sync_api import sync_playwright

def scrapeHNews(page):
    page.goto("https://news.ycombinator.com/")
    items = page.locator("span.titleline").all()
    for item in items:
        print(item.text_content())
    

with sync_playwright() as p:
    browser = p.firefox.launch(headless=False)   
    page = browser.new_page()
    page.goto("https://playwright.dev/python/")
    print(page.title())
    scrapeHNews(page)
    
    while True:
        pass
