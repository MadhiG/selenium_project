"""Sample Selenium test using the helper module.
Run with: `pytest -s tests/test_sample.py`
"""

from src.browser import get_driver

def test_google_homepage():
    driver = get_driver()
    driver.get("https://www.google.com")
    assert "Google" in driver.title
    driver.quit()
