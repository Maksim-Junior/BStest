from selenium.common.exceptions import TimeoutException
from .click_page import SearchClick
from .loaddelay_page import SearchLoadDelay
from .verifytext_page import SearchVerifyText
from .visibility_page import SearchHelpVisibility
from .classattr_page import SearchHelpClassAttr
from .clientdelay_page import SearchHelpClientDelay
from .dynamictable_page import SearchDynamicTable
from .sampleapp_page import SearchSampleApp
from .hiddenlayers_page import SearchHiddenLayers
from .mouseover_page import SearchMouseOver
from selenium.common.exceptions import ElementClickInterceptedException
import allure
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
binary_location = "/usr/bin/google-chrome"
option = webdriver.ChromeOptions()
option.add_argument('--headless')
option.add_argument('--no-sandbox')
option.binary_location = binary_location


class PlayGround(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=driver_location, chrome_options=option)
        # self.drivers = webdriver.Remote(
        #   command_executor="http://0.0.0.0:4444/wd/hub",
        #  desired_capabilities=capabilities
        # )
        self.driver.implicitly_wait(10)

    @allure.feature('Testing UI PlayGround')
    @allure.story('Test - mouse over')
    def test_mouseover(self):
        resource = "mouseover"
        browser = self.driver
        page = SearchMouseOver(browser)
        with allure.step('Go to the site'):
            page.go_to_site(resource)
        with allure.step('Find count of click'):
            first_count = page.find_click_count()
        with allure.step('Click the link'):
            page.double_click_link()
        with allure.step('Find count of click'):
            second_count = page.find_click_count()
        with allure.step('Check: first count == second count'):
            self.assertEqual(int(second_count) - int(first_count), 2)

    @allure.feature('Testing UI PlayGround')
    @allure.story('Test - visibility')
    def test_visibility(self):
        resource = "visibility"
        browser = self.driver
        page = SearchHelpVisibility(browser)
        with allure.step('Go to the site'):
            page.go_to_site(resource)
        with allure.step('Check to button not remove'):
            button = page.check_button_remove()
        self.assertTrue(button)
        with allure.step('Click the "Hide" button'):
            page.click_button()

        try:
            with allure.step('Check to button remove'):
                remove = page.check_button_remove()
        except TimeoutException:
            remove = False
        self.assertFalse(remove)

        with allure.step('Check to button - zero width'):
            button_zero_width = page.check_button_zero_width()
        with allure.step('Check to button - displayed'):
            width = button_zero_width.is_displayed()
        self.assertFalse(width)
        with allure.step('Check to button - overlapped'):
            self.assertRaises(ElementClickInterceptedException, page.check_button_overlapped)

        with allure.step('Check to button - zero opacity'):
            button_zero_opacity = page.check_button_zero_opacity()
        with allure.step('Check to button - displayed'):
            opacity = button_zero_opacity.is_displayed()
        self.assertFalse(opacity)

        with allure.step('Check to button - invisible'):
            button_invisible = page.check_button_invisible()
        with allure.step('Check to button - displayed'):
            invisible = button_invisible.is_displayed()
        self.assertFalse(invisible)

        with allure.step('Check to button - display none'):
            button_display_none = page.check_button_display_none()
        with allure.step('Check to button - displayed'):
            display = button_display_none.is_displayed()
        self.assertFalse(display)

        with allure.step('Check to button - button offscreen'):
            button_display_offscreen = page.check_button_offscreen()
        with allure.step('Check to button - displayed'):
            offscreen = button_display_offscreen.is_displayed()
        self.assertFalse(offscreen)

    @allure.feature('Testing UI PlayGround')
    @allure.story('Test - class attribute')
    def test_classattr(self):
        resource = "classattr"
        browser = self.driver
        page = SearchHelpClassAttr(browser)
        with allure.step('Go to the site'):
            page.go_to_site(resource)

        with allure.step('Click the button'):
            page.click_button()
        with allure.step('Switch to alert and accept'):
            page.switch_to_alert_accept()
        with allure.step('Test the button'):
            button = page.test_button()
        self.assertTrue(button)

    @allure.feature('Testing UI PlayGround')
    @allure.story('Test - client delay')
    def test_clientdelay(self):
        resource = "clientdelay"
        browser = self.driver
        page = SearchHelpClientDelay(browser)
        with allure.step('Go to the site'):
            page.go_to_site(resource)

        with allure.step('Click the button'):
            page.click_button()
        with allure.step('Wait the text'):
            button = page.wait_to_text()
        self.assertTrue(button)

    @allure.feature('Testing UI PlayGround')
    @allure.story('Test - dynamic table')
    def test_dynamictable(self):
        resource = "dynamictable"
        browser = self.driver
        page = SearchDynamicTable(browser)
        with allure.step('Go to the site'):
            page.go_to_site(resource)
        with allure.step('Find the table with CPU'):
            chrome_cpu = page.chrome_cpu()
        with allure.step('Select all processes'):
            tasks = page.tasks()
        list_task = tasks.text.split("\n")
        chrome_task = [chrome for chrome in list_task if chrome.startswith("Chrome")]
        chrome_detail_list = chrome_task[0].split()
        cpu = [cpu for cpu in chrome_detail_list if '%' in cpu]
        self.assertEqual(chrome_cpu, f'{chrome_detail_list[0]} CPU: {cpu[0]}')

    @allure.feature('Testing UI PlayGround')
    @allure.story('Test - sample app')
    def test_sampleapp(self):
        resource = "sampleapp"
        browser = self.driver
        page = SearchSampleApp(browser)
        with allure.step('Go to the site'):
            page.go_to_site(resource)
        with allure.step('Status of authorisation'):
            login_status = page.login_status()
        self.assertEqual(login_status, 'User logged out.')

        with allure.step('Enter username'):
            username = page.enter_username()
        with allure.step('Enter password'):
            page.enter_password()
        with allure.step('Login'):
            page.click_login()
        with allure.step('Status of authorisation'):
            login_status = page.login_status()
        self.assertEqual(login_status, f'Welcome, {username}!')

    @allure.feature('Testing UI PlayGround')
    @allure.story('Test - hidden layers')
    def test_hiddenlayers(self):
        resource = "hiddenlayers"
        browser = self.driver
        page = SearchHiddenLayers(browser)
        with allure.step('Go to the site'):
            page.go_to_site(resource)

        with allure.step('First click the button'):
            first_click = page.click_button()
        self.assertTrue(first_click)

        with allure.step('Second click the button'):
            second_click = page.click_button()
        self.assertFalse(second_click)

    @allure.feature('Testing UI PlayGround')
    @allure.story('Test - click')
    def test_click(self):
        resource = "click"
        browser = self.driver
        page = SearchClick(browser)
        with allure.step('Go to the site'):
            page.go_to_site(resource)
        with allure.step('Click the button'):
            page.click_button()

        with allure.step('Check to the button is clickable'):
            button = page.click_button()
        self.assertTrue(button)

    @allure.feature('Testing UI PlayGround')
    @allure.story('Test - verify text')
    def test_verifytext(self):
        resource = "verifytext"
        browser = self.driver
        page = SearchVerifyText(browser)
        with allure.step('Go to the site'):
            page.go_to_site(resource)

        with allure.step('Search the text'):
            text = page.search_text()
        self.assertEqual(text, "Welcome UserName!")

    @allure.feature('Testing UI PlayGround')
    @allure.story('Test - load delay')
    def test_loaddelay(self):
        browser = self.driver
        page = SearchLoadDelay(browser)
        with allure.step('Go to the site'):
            page.go_to_site()
        with allure.step('Click the link'):
            page.click_link()
        with allure.step('Wait and click the button'):
            click_button = page.wait_and_click_button()
        self.assertTrue(click_button)

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
