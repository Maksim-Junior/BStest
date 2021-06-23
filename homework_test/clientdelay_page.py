from .baseApp import Base
from selenium.webdriver.common.by import By


class Locators:
    BUTTON = (By.ID, 'ajaxButton')
    TEXT = (By.CLASS_NAME, 'bg-success')


class SearchHelpClientDelay(Base):
    def click_button(self):
        return self.find_element(Locators.BUTTON, time=2).click()

    def wait_to_text(self):
        return self.find_element(Locators.TEXT, time=15)
