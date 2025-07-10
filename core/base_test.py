import pytest
from selenium import webdriver

@pytest.fixture(scope='session')
def browser():
    options = webdriver.ChromeOptions()
    options.add_argument('--lang=ru')
    driver = webdriver.Remote(command_executor="https://5.35.85.102:4444", options=options)
    yield driver
    if driver:
        driver.quit()