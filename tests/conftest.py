import pytest
from selenium import webdriver

@pytest.fixture
def browser():
    driver = webdriver.Chrome()  # launches Chrome
    driver.maximize_window()     # makes window full screen
    yield driver                 # gives the browser to test
    driver.quit()                # closes the browser
