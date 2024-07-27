import sqlite3, playwright, nltk, flask, nest_asyncio, parsel, bs4, pandas, time
from playwright.sync_api import sync_playwright
import playwright.sync_api


connection = sqlite3.connect("Scrape.db")
cursor = connection.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS posts (url TEXT PRIMARY KEY, text TEXT)")


def text_to_db(page, url):
    try:
        page.wait_for_selector("body")
        text = page.locator("body").inner_text()
        return text
    except Exception as e:
        print(f'Error extracting text from {url}: {e}')
        return None

with sync_playwright() as pw:
    home_page = "https://www.reddit.com/r/wallstreetbets/"
    browser = pw.chromium.launch(headless=False, channel="chrome")
    context = browser.new_context(viewport={"width": 1920, "height": 1080})
    page = context.new_page()
    page.goto(home_page)

    while True:
        links = page.locator("a")

        for link in links.all():
            href = links.get_attribute("href")

            with page.context.expect_page() as new_page_info:
                link.click()
            new_page = new_page_info.value

            text = text_to_db(new_page, href)
            if text:
                try:
                    cursor.execute("INSERT INTO posts VALUES (?, ?)", (href, text))
                    connection.commit()
                except sqlite3.IntegrityError:
                    print(f'URL already in database: {href}')
            
            new_page.close()
            time.sleep(100)
            
        break

    browser.close()
    connection.close()

