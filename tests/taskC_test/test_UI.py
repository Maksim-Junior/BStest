import pytest
from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys


# Task 3(c)
# UI tests for https://www.metric-conversions.org/:
# - Test for converting Celsius to Fahrenheit temperature;
# - Test for converting meters to feet;
# - Test for converting ounces to grams;

@pytest.fixture
def browser():
    driver = Chrome()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()


def test_celsius_to_fahrenheit(browser):
    url = 'https://www.metric-conversions.org/temperature/celsius-to-fahrenheit.htm'
    celsius = '10'

    browser.get(url)

    search_input = browser.find_element_by_id('argumentConv')
    search_input.send_keys(celsius + Keys.RETURN)

    answer = browser.find_element_by_id('answer').text

    assert answer == '10°C= 50.00000°F'


def test_celsius_to_fahrenheit_negative(browser):
    url = 'https://www.metric-conversions.org/temperature/celsius-to-fahrenheit.htm'
    celsius = '-30'

    browser.get(url)

    search_input = browser.find_element_by_id('argumentConv')
    search_input.send_keys(celsius + Keys.RETURN)

    answer = browser.find_element_by_id('answer').text

    assert answer == '-30°C= -22.00000°F'


def test_celsius_to_fahrenheit_null(browser):
    url = 'https://www.metric-conversions.org/temperature/celsius-to-fahrenheit.htm'
    celsius = '0'

    browser.get(url)

    search_input = browser.find_element_by_id('argumentConv')
    search_input.send_keys(celsius + Keys.RETURN)

    answer = browser.find_element_by_id('answer').text

    assert answer == '0°C= 32.00000°F'


def test_celsius_to_fahrenheit_bigInt(browser):
    url = 'https://www.metric-conversions.org/temperature/celsius-to-fahrenheit.htm'
    celsius = '9999999999'

    browser.get(url)

    search_input = browser.find_element_by_id('argumentConv')
    search_input.send_keys(celsius + Keys.RETURN)

    answer = browser.find_element_by_id('answer').text

    assert answer == '9999999999°C= 1.800000e+10°F'


def test_meters_to_feet(browser):
    url = 'https://www.metric-conversions.org/length/meters-to-feet.htm'
    celsius = '20'

    browser.get(url)

    search_input = browser.find_element_by_id('argumentConv')
    search_input.send_keys(celsius + Keys.RETURN)

    answer = browser.find_element_by_id('answer').text

    assert answer == '20m= 65ft 7.401576in'


def test_meters_to_feet_negative(browser):
    url = 'https://www.metric-conversions.org/length/meters-to-feet.htm'
    celsius = '-50'

    browser.get(url)

    search_input = browser.find_element_by_id('argumentConv')
    search_input.send_keys(celsius + Keys.RETURN)

    answer = browser.find_element_by_id('answer').text

    assert answer == '-50m= -164ft -0.5039400in'


def test_meters_to_feet_null(browser):
    url = 'https://www.metric-conversions.org/length/meters-to-feet.htm'
    celsius = '0'

    browser.get(url)

    search_input = browser.find_element_by_id('argumentConv')
    search_input.send_keys(celsius + Keys.RETURN)

    answer = browser.find_element_by_id('answer').text

    assert answer == '0m= 0ft 0.000000in'


def test_meters_to_feet_bigInt(browser):
    url = 'https://www.metric-conversions.org/length/meters-to-feet.htm'
    celsius = '99999999'

    browser.get(url)

    search_input = browser.find_element_by_id('argumentConv')
    search_input.send_keys(celsius + Keys.RETURN)

    answer = browser.find_element_by_id('answer').text

    assert answer == '99999999m= 328083986ft 8.629922in'


def test_ounces_to_grams(browser):
    url = 'https://www.metric-conversions.org/weight/ounces-to-grams.htm'
    celsius = '15'

    browser.get(url)

    search_input = browser.find_element_by_id('argumentConv')
    search_input.send_keys(celsius + Keys.RETURN)

    answer = browser.find_element_by_id('answer').text

    assert answer == '15oz= 425.2428g'


def test_ounces_to_grams_negative(browser):
    url = 'https://www.metric-conversions.org/weight/ounces-to-grams.htm'
    celsius = '-10'

    browser.get(url)

    search_input = browser.find_element_by_id('argumentConv')
    search_input.send_keys(celsius + Keys.RETURN)

    answer = browser.find_element_by_id('answer').text

    assert answer == '-10oz= -283.4952g'


def test_ounces_to_grams_null(browser):
    url = 'https://www.metric-conversions.org/weight/ounces-to-grams.htm'
    celsius = '0'

    browser.get(url)

    search_input = browser.find_element_by_id('argumentConv')
    search_input.send_keys(celsius + Keys.RETURN)

    answer = browser.find_element_by_id('answer').text

    assert answer == '0oz= 0.000000g'


def test_ounces_to_grams_bigInt(browser):
    url = 'https://www.metric-conversions.org/weight/ounces-to-grams.htm'
    celsius = '99999999999'

    browser.get(url)

    search_input = browser.find_element_by_id('argumentConv')
    search_input.send_keys(celsius + Keys.RETURN)

    answer = browser.find_element_by_id('answer').text

    assert answer == '99999999999oz= 2.834952e+12g'
