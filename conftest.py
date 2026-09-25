import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

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
    options = Options()
    options.add_argument("--headless=new")
    options.add_argument("--window-size=1440,900")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")

    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(2)
    yield driver
    driver.quit()
