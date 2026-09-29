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

def scrapeTechCrunch(page):
    page.goto("https://techcrunch.com/latest/")
    items = page.locator("a.loop-card__title-link").all()
    for item in items:
        print(item.text_content())

with sync_playwright() as p:
    browser = p.firefox.launch(headless=False)   
    page = browser.new_page()
    print("YCombinator:-")
    scrapeYCombinator(page)
    print()
    print("HackerNews:-")
    scrapeHNews(page)
    print()
    print("Tech Crunch:-")
    scrapeTechCrunch(page)
    print()
    
    while True:
        pass
