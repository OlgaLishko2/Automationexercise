import pytest
from playwright.sync_api import sync_playwright

def test_title():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)  # headless=True to hide browser
        page = browser.new_page()
        page.goto("https://example.com")
        assert "Example Domain" in page.title()
        browser.close()
