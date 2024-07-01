import sqlite3, playwright, nltk, flask, nest_asyncio
from playwright.sync_api import sync_playwright
import playwright.sync_api

nest_asyncio.apply()
pw = sync_playwright().start()
browser = pw.chromium.launch(headless=False)
page = browser.new_page()
page.goto("https://scrapfly.io/blog/web-scraping-with-playwright-and-python/")



