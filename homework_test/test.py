from selenium.common.exceptions import TimeoutException

from .click_page import SearchClick
from .verifytext_page import SearchVerifyText
from .visibility_page import SearchHelpVisibility
from .classattr_page import SearchHelpClassAttr
from .clientdelay_page import SearchHelpClientDelay
from .dynamictable_page import SearchDynamicTable
from .sampleapp_page import SearchSampleApp
from .hiddenlayers_page import SearchHiddenLayers


def test_visibility(browser):
    resource = "visibility"
    page = SearchHelpVisibility(browser)
    page.go_to_site(resource)

    button = page.check_button_remove()
    assert button

    page.click_button()

    try:
        remove = page.check_button_remove()
    except TimeoutException:
        remove = False
    assert not remove

    button_zero_width = page.check_button_zero_width()
    width = button_zero_width.is_displayed()
    assert not width

    button_overlapped = page.check_button_overlapped()
    assert not button_overlapped

    button_zero_opacity = page.check_button_zero_opacity()
    opacity = button_zero_opacity.is_displayed()
    assert not opacity

    button_invisible = page.check_button_invisible()
    invisible = button_invisible.is_displayed()
    assert not invisible

    button_display_none = page.check_button_display_none()
    display = button_display_none.is_displayed()
    assert not display

    button_display_offscreen = page.check_button_offscreen()
    offscreen = button_display_offscreen.is_displayed()
    assert not offscreen


def test_classattr(browser):
    resource = "classattr"
    page = SearchHelpClassAttr(browser)
    page.go_to_site(resource)

    page.click_button()
    page.switch_to_alert_accept()
    button = page.test_button()
    assert button


def test_clientdelay(browser):
    resource = "clientdelay"
    page = SearchHelpClientDelay(browser)
    page.go_to_site(resource)

    page.click_button()
    button = page.wait_to_text()
    assert button


def test_dynamictable(browser):
    resource = "dynamictable"
    page = SearchDynamicTable(browser)
    page.go_to_site(resource)
    chrome_cpu = page.chrome_cpu()
    tasks = page.tasks()
    list_task = tasks.text.split("\n")
    chrome_task = [chrome for chrome in list_task if chrome.startswith("Chrome")]
    chrome_detail_list = chrome_task[0].split()
    cpu = [cpu for cpu in chrome_detail_list if '%' in cpu]
    assert chrome_cpu == f'{chrome_detail_list[0]} CPU: {cpu[0]}'


def test_sampleapp(browser):
    resource = "sampleapp"
    page = SearchSampleApp(browser)
    page.go_to_site(resource)
    login_status = page.login_status()
    assert login_status == 'User logged out.'

    username = page.enter_username()
    page.enter_password()
    page.click_login()
    login_status = page.login_status()
    assert login_status == f'Welcome, {username}!'


def test_hiddenlayers(browser):
    resource = "hiddenlayers"
    page = SearchHiddenLayers(browser)
    page.go_to_site(resource)

    first_click = page.click_button()
    assert first_click

    second_click = page.click_button()
    assert not second_click


def test_click(browser):
    resource = "click"
    page = SearchClick(browser)
    page.go_to_site(resource)
    page.click_button()

    button = page.click_button()
    assert button


def test_verifytext(browser):
    resource = "verifytext"
    page = SearchVerifyText(browser)
    page.go_to_site(resource)

    text = page.search_text()
    assert text == "Welcome UserName!"
