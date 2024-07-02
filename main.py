import sqlite3, playwright, nltk, flask, nest_asyncio, parsel
from playwright.sync_api import sync_playwright
import playwright.sync_api

'''
nest_asyncio.apply()
pw = sync_playwright().start()
browser = pw.chromium.launch(headless=False)
page = browser.new_page()
page.goto("https://scrapfly.io/blog/web-scraping-with-playwright-and-python/")
'''


with sync_playwright() as pw:
    browser = pw.chromium.launch(headless=False)
    context = browser.new_context(viewport={"width": 1920, "height": 1080})
    page = context.new_page()
    page.goto("https://scrapfly.io/blog/web-scraping-with-playwright-and-python/")
    page.wait_for_selector()
    print(page.content())
    
    