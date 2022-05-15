import requests

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from elements.base_elements import BaseElements
from src.enums import *
from locators import *

from tools import Logger
from tools import MouseKeyboardActions
from tools.allure_screenshot import taking_screenshot

RESPONSE_STATUS_200 = 200
RESPONSE_STATUS_404 = 404


class BasePage:

    def __init__(self, browser=None, url=None):
        self.browser = browser
        self.url = url
        self.base_element = BaseElements()
        self.mouse_keyboard_actions = MouseKeyboardActions(self.browser)

    def check_is_displayed(self, locator, element):
        Logger().info(f"Check is displayed element: {element}.")
        value = BaseElements.find_element(
            self.browser, locator, element).is_displayed()
        assert value is True, \
            (GlobalErrorMessages.WRONG_IS_DISPLAYED.value,
             taking_screenshot(self.browser))

    def checks_page_response_404(self):
        url = self.get_url()
        response = requests.get(url=url)
        assert response.status_code == RESPONSE_STATUS_404,\
            GlobalErrorMessages.WRONG_STATUS_CODE.value
        assert self.url == url, LoginPageErrorMessages.WRONG_PAGE.value

    def click_element(self, locator, element):
        Logger().info(f"Click element: {element}.")
        return self.base_element.click(
            self.base_element.find_element(self.browser, locator, element))

    def enter_value(self, locator, element, name):
        Logger().info(f"Enter value(Element: {element}, name: {name}).")
        value = self.base_element.find_element(
            self.browser, locator, element)
        self.base_element.click(value)
        self.mouse_keyboard_actions.enter_text(name)

    def get_url(self):
        return self.browser.current_url

    def get_text(self, locator, element):
        Logger().info(f"Get text from element: {element}.")
        return self.base_element.get_text(
            self.base_element.find_element(self.browser, locator, element))

    def open_page(self):
        Logger().info(f"Open page: {self.url}.")
        self.browser.get(self.url)

    def page_response(self):
        response = requests.get(url=self.url)
        assert response.status_code == RESPONSE_STATUS_200,\
            GlobalErrorMessages.WRONG_STATUS_CODE.value

    def wait_element_to_be_clickable(self, locator, element, time=10):
        Logger().info(f"Wait element to be clickable(Element: {element}).")
        value = BaseElements.find_element(self.browser, locator, element)
        WebDriverWait(self.browser, time).until(
            EC.element_to_be_clickable(value))
