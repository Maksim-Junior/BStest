from selenium.common.exceptions import ElementClickInterceptedException

from baseApp import Base
from selenium.webdriver.common.by import By


class Locators:
    LINK = (By.XPATH, "//*[contains(text(), 'Load Delay') and @href='/loaddelay']")
    BUTTON = (By.XPATH, "//*[contains(text(), 'Button Appearing After Delay') and @class='btn btn-primary']")


class SearchLoadDelay(Base):
    def click_link(self):
        return self.find_element(Locators.LINK, time=2).click()

    def wait_and_click_button(self):
        try:
            self.find_element(Locators.BUTTON, time=10).click()
            answer = True
        except ElementClickInterceptedException:
            answer = False
        return answer

