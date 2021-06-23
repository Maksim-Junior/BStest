from .baseApp import Base
from selenium.webdriver.common.by import By


class Locators:
    BUTTON_HIDE = (By.ID, 'hideButton')
    BUTTON_REMOVE = (By.ID, 'removedButton')
    BUTTON_ZERO_WIDTH = (By.ID, 'zeroWidthButton')
    BUTTON_OVERLAPPED = (By.ID, 'overlappedButton')
    BUTTON_ZERO_OPACITY = (By.ID, 'transparentButton')
    BUTTON_INVISIBLE = (By.ID, 'invisibleButton')
    BUTTON_NOT_DISPLAYED = (By.ID, 'notdisplayedButton')
    BUTTON_OFFSCREEN = (By.ID, 'offscreenButton')


class SearchHelpVisibility(Base):
    def click_button(self):
        return self.find_element(Locators.BUTTON_HIDE, time=2).click()

    def check_button_remove(self):
        return self.find_element(Locators.BUTTON_REMOVE, time=2)

    def check_button_zero_width(self):
        return self.find_element(Locators.BUTTON_ZERO_WIDTH, time=2)

    def check_button_overlapped(self):
        return self.find_element(Locators.BUTTON_OVERLAPPED, time=2).click()

    def check_button_zero_opacity(self):
        return self.find_element(Locators.BUTTON_ZERO_OPACITY, time=2)

    def check_button_invisible(self):
        return self.find_element(Locators.BUTTON_INVISIBLE, time=2)

    def check_button_display_none(self):
        return self.find_element(Locators.BUTTON_NOT_DISPLAYED, time=2)

    def check_button_offscreen(self):
        return self.find_element(Locators.BUTTON_OFFSCREEN, time=2)
