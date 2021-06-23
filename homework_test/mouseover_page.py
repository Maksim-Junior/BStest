from .baseApp import Base
from selenium.webdriver.common.by import By


class Locators:
    LINK = (By.XPATH, "//*[contains(text(), 'Click me')]")
    CLICK_COUNT = (By.ID, 'clickCount')


class SearchMouseOver(Base):
    def double_click_link(self):
        link = self.find_element(Locators.LINK, time=2)
        link.click()
        link = self.find_element(Locators.LINK, time=2)
        link.click()
        return link

    def find_click_count(self):
        return self.find_element(Locators.CLICK_COUNT, time=2).text
