from selenium.common.exceptions import TimeoutException
from click_page import SearchClick
from loaddelay_page import SearchLoadDelay
from verifytext_page import SearchVerifyText
from visibility_page import SearchHelpVisibility
from classattr_page import SearchHelpClassAttr
from clientdelay_page import SearchHelpClientDelay
from dynamictable_page import SearchDynamicTable
from sampleapp_page import SearchSampleApp
from hiddenlayers_page import SearchHiddenLayers
from mouseover_page import SearchMouseOver
from selenium.common.exceptions import ElementClickInterceptedException

import unittest
from selenium import webdriver

capabilities = {
    "browserName": "chrome",
    "browserVersion": "91.0",
    "selenoid:options": {
        "enableVNC": True,
        "enableVideo": False
    }
}

driver_location = "/usr/bin/chromedriver"
binary_location = "usr/bin/google-chrome"
option = webdriver.ChromeOptions()
option.binary_location = binary_location


class PlayGround(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=driver_location, chrome_options=option)
        # self.drivers = webdriver.Remote(
        #   command_executor="http://0.0.0.0:4444/wd/hub",
        #  desired_capabilities=capabilities
        # )
        self.driver.implicitly_wait(10)

    def test_mouseover(self):
        resource = "mouseover"
        browser = self.driver
        page = SearchMouseOver(browser)
        page.go_to_site(resource)
        first_count = page.find_click_count()
        page.double_click_link()
        second_count = page.find_click_count()
        self.assertEqual(int(second_count) - int(first_count), 2)

    def test_visibility(self):
        resource = "visibility"
        browser = self.driver
        page = SearchHelpVisibility(browser)
        page.go_to_site(resource)

        button = page.check_button_remove()
        self.assertTrue(button)

        page.click_button()

        try:
            remove = page.check_button_remove()
        except TimeoutException:
            remove = False
        self.assertFalse(remove)

        button_zero_width = page.check_button_zero_width()
        width = button_zero_width.is_displayed()
        self.assertFalse(width)

        self.assertRaises(ElementClickInterceptedException, page.check_button_overlapped)

        button_zero_opacity = page.check_button_zero_opacity()
        opacity = button_zero_opacity.is_displayed()
        self.assertFalse(opacity)

        button_invisible = page.check_button_invisible()
        invisible = button_invisible.is_displayed()
        self.assertFalse(invisible)

        button_display_none = page.check_button_display_none()
        display = button_display_none.is_displayed()
        self.assertFalse(display)

        button_display_offscreen = page.check_button_offscreen()
        offscreen = button_display_offscreen.is_displayed()
        self.assertFalse(offscreen)

    def test_classattr(self):
        resource = "classattr"
        browser = self.driver
        page = SearchHelpClassAttr(browser)
        page.go_to_site(resource)

        page.click_button()
        page.switch_to_alert_accept()
        button = page.test_button()
        self.assertTrue(button)

    def test_clientdelay(self):
        resource = "clientdelay"
        browser = self.driver
        page = SearchHelpClientDelay(browser)
        page.go_to_site(resource)

        page.click_button()
        button = page.wait_to_text()
        self.assertTrue(button)

    def test_dynamictable(self):
        resource = "dynamictable"
        browser = self.driver
        page = SearchDynamicTable(browser)
        page.go_to_site(resource)
        chrome_cpu = page.chrome_cpu()
        tasks = page.tasks()
        list_task = tasks.text.split("\n")
        chrome_task = [chrome for chrome in list_task if chrome.startswith("Chrome")]
        chrome_detail_list = chrome_task[0].split()
        cpu = [cpu for cpu in chrome_detail_list if '%' in cpu]
        self.assertEqual(chrome_cpu, f'{chrome_detail_list[0]} CPU: {cpu[0]}')

    def test_sampleapp(self):
        resource = "sampleapp"
        browser = self.driver
        page = SearchSampleApp(browser)
        page.go_to_site(resource)
        login_status = page.login_status()
        self.assertEqual(login_status, 'User logged out.')

        username = page.enter_username()
        page.enter_password()
        page.click_login()
        login_status = page.login_status()
        self.assertEqual(login_status, f'Welcome, {username}!')

    def test_hiddenlayers(self):
        resource = "hiddenlayers"
        browser = self.driver
        page = SearchHiddenLayers(browser)
        page.go_to_site(resource)

        first_click = page.click_button()
        self.assertTrue(first_click)

        second_click = page.click_button()
        self.assertFalse(second_click)

    def test_click(self):
        resource = "click"
        browser = self.driver
        page = SearchClick(browser)
        page.go_to_site(resource)
        page.click_button()

        button = page.click_button()
        self.assertTrue(button)

    def test_verifytext(self):
        resource = "verifytext"
        browser = self.driver
        page = SearchVerifyText(browser)
        page.go_to_site(resource)

        text = page.search_text()
        self.assertEqual(text, "Welcome UserName!")

    def test_loaddelay(self):
        browser = self.driver
        page = SearchLoadDelay(browser)
        page.go_to_site()
        page.click_link()
        click_button = page.wait_and_click_button()
        self.assertTrue(click_button)

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
