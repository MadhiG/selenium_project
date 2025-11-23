"""Selenium helper utilities for easy test setup.
Provides a function to create a WebDriver instance with optional headless mode.
"""

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import os

def get_driver(headless: bool = True):
    """Return a configured Chrome WebDriver.
    Args:
        headless: Run Chrome in headless mode if True.
    """
    chrome_options = Options()
    if headless:
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--disable-gpu")
    # Use webdriver_manager to download and manage ChromeDriver automatically
    driver_path = ChromeDriverManager().install()
    service = ChromeService(executable_path=driver_path)
    driver = webdriver.Chrome(service=service, options=chrome_options)
    driver.implicitly_wait(10)
    return driver
