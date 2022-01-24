from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from elements.base_elements import BaseElements
from locators import Base
from tools import Logger
from tools import MouseKeyboardActions
from tools import AllureScreenshot


class BasePage:

    def __init__(self):
        self.base_element = BaseElements()

    def open_page(self, browser, link):
        Logger().info(f"Open page: {link}.")
        browser.get(link)

    def get_url(self, browser):
        return browser.current_url

    def get_text(self, browser, locator, element):
        Logger().info(f"Get text from element: {element}.")
        return self.base_element._get_text(
            self.base_element._find_element(browser, locator, element))

    def wait_element_to_be_clickable(self, browser, locator, element):
        Logger().info(f"Wait element to be clickable(Element: {element}).")
        value = BaseElements._find_element(browser, locator, element)
        return WebDriverWait(browser, Base.TIME).until(
            EC.element_to_be_clickable(value))

    def check_is_displayed(self, browser, locator, element):
        Logger().info(f"Check is displayed element: {element}.")
        __implicitly_wait_time = 1
        browser.implicitly_wait(__implicitly_wait_time)
        try:
            BaseElements._find_element(browser, locator, element).\
                is_displayed()
        except NoSuchElementException:
            return False
        return True

    def click_element(self, browser, locator, element):
        Logger().info(f"Click element: {element}.")
        return self.base_element._click(
            self.base_element._find_element(browser, locator, element))

    def enter_value(self, browser, locator, element, name):
        Logger().info(f"Enter value(Element: {element}, name: {name}).")
        value = self.base_element._find_element(
            browser, locator, element)
        click = self.base_element._click(value)
        MouseKeyboardActions()._enter_text(browser, name)

