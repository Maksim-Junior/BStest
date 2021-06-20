from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Base:
    def __init__(self, driver):
        self.driver = driver
        self.base_url = 'http://uitestingplayground.com/'

    def find_element(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator),
                                                      message=f"Can't find elements by locator {locator}")

    def go_to_site(self, resource):
        return self.driver.get(f'{self.base_url}{resource}')

    def switch_to_alert_accept(self):
        return self.driver.switch_to_alert().accept()
