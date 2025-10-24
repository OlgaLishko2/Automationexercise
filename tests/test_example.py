
from config.links import Links

def test_title(page):
    page.goto(Links.HOST)
    assert "Automation Exercise" in page.title()

