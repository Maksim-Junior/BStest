from baseApp import Base
from selenium.webdriver.common.by import By


class Locators:
    BUTTON_BLUE = (By.XPATH, "//button[contains(concat(' ', normalize-space(@class), ' '), ' btn-primary ')]")
    TEST_BUTTON_BLUE = (By.CLASS_NAME, 'btn-primary')


class SearchHelpClassAttr(Base):
    def click_button(self):
        return self.find_element(Locators.BUTTON_BLUE, time=2).click()

    def test_button(self):
        return self.find_element(Locators.TEST_BUTTON_BLUE, time=2)
