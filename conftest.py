import os
import re

import pytest
from selenium import webdriver

from config.settings import BASE_URL, API_URL, DB_PATH
from utils.api_client import APIClient


@pytest.fixture
def base_url():
    return BASE_URL


@pytest.fixture
def api_client():
    return APIClient(API_URL)


@pytest.fixture
def db_path():
    return DB_PATH


@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")

    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(2)

    yield driver

    driver.quit()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """
    Capture a screenshot automatically when a Selenium UI test fails.
    """
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed and "driver" in item.funcargs:
        driver = item.funcargs["driver"]

        screenshot_dir = os.path.join("reports", "screenshots")
        os.makedirs(screenshot_dir, exist_ok=True)

        # Create a safe filename from the pytest test name.
        test_name = re.sub(r"[^a-zA-Z0-9_-]", "_", item.nodeid)
        screenshot_path = os.path.join(
            screenshot_dir,
            f"{test_name}.png"
        )

        driver.save_screenshot(screenshot_path)

        print(f"\nFailure screenshot saved: {screenshot_path}")