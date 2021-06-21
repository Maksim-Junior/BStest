from baseApp import Base
from selenium.webdriver.common.by import By


class Locators:
    VERIFY_TEXT = (By.XPATH, "//span[normalize-space(.)='Welcome UserName!']")


class SearchVerifyText(Base):
    def search_text(self):
        return self.find_element(Locators.VERIFY_TEXT, time=2).text
