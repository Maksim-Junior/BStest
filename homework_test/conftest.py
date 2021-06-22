import pytest
from selenium import webdriver

capabilities = {
    "browserName": "chrome",
    "browserVersion": "91.0",
    "selenoid:options": {
        "enableVNC": True,
        "enableVideo": False
    }
}


@pytest.fixture
def browser():
    driver = webdriver.Remote(
        command_executor="http://0.0.0.0:4444/wd/hub",
        desired_capabilities=capabilities)
    driver.implicitly_wait(10)
    yield driver
    driver.quit()
