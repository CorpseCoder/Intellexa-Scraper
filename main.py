from playwright.sync_api import sync_playwright

def scrapeYCombinator(page):
    page.goto("https://news.ycombinator.com/")
    items = page.locator("span.titleline").all()
    for item in items:
        print(item.text_content())

def scrapeHNews(page):
    page.goto("https://thehackernews.com/")
    items = page.locator("div.pop-title").all()
    for item in items:
        print(item.text_content())

with sync_playwright() as p:
    browser = p.firefox.launch(headless=False)   
    page = browser.new_page()
    print("YCombinator:-")
    scrapeYCombinator(page)
    print("HackerNews:-")
    scrapeHNews(page)
    
    while True:
        pass
