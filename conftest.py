import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture()
def browser():
    browser = webdriver.Chrome()
    yield browser
    browser.quit()
