import sqlite3, playwright, nltk, flask, nest_asyncio, parsel
from playwright.sync_api import sync_playwright
import playwright.sync_api

scrape_results_database = sqlite3.connect("Scrape.db")
'''
nest_asyncio.apply()
pw = sync_playwright().start()
browser = pw.chromium.launch(headless=False)
page = browser.new_page()
page.goto("https://scrapfly.io/blog/web-scraping-with-playwright-and-python/")
'''


# 1. open reddit WSB home page in chrome
def run(playwright: playwright):
    home_page = "https://www.reddit.com/r/wallstreetbets/"
    browser = playwright.chromium.launch(headless=False, channel="chrome")
    context = browser.new_context(viewport={"width": 1920, "height": 1080})
    page = context.new_page()
    page.goto(home_page)
    page.wait_for_selector()
    sqlite3.a


with sync_playwright() as playwright:
    run(playwright)