import pytest
from playwright.sync_api import Page, expect
import random, string

def random_email():
    email_name = ''.join(random.choices(string.ascii_lowercase + string.digits, k=4))
    return f"new_{email_name}@example.com"

@pytest.fixture(autouse=True)
def go_to_signup(page: Page):
    page.goto("https://automationexercise.com/login")

    # Закрыть popup "consent"
    if page.locator("button:has-text('Consent')").is_visible():
        page.locator("button:has-text('Consent')").click()


def test_register_new_user(page: Page):
    name = "TestUser"
    email = random_email()

    page.locator("input[data-qa='signup-name']").fill(name)
    page.locator("input[data-qa='signup-email']").fill(email)
    page.locator("button[data-qa='signup-button']").click()

    expect(page.locator("text=Enter Account Information")).to_be_visible()
