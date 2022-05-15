from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class MouseKeyboardActions:

    def __init__(self, browser):
        self.browser = browser

    def click_arrow_up(self):
        webdriver.ActionChains(self.browser).send_keys(Keys.ARROW_UP)

    def click_arrow_down(self):
        webdriver.ActionChains(self.browser).send_keys(Keys.ARROW_DOWN).perform()

    def click_enter(self):
        webdriver.ActionChains(self.browser).send_keys(Keys.ENTER).perform()

    def click_tab(self):
        webdriver.ActionChains(self.browser).send_keys(Keys.TAB).perform()

    @staticmethod
    def delete_text(element):
        element.send_keys(Keys.DELETE)

    def double_click(self, value):
        webdriver.ActionChains(self.browser).double_click(value).perform()

    def do_key_down(self):
        webdriver.ActionChains(self.browser).key_down(Keys.SHIFT)

    def enter_text(self, text):
        webdriver.ActionChains(self.browser).send_keys(text).perform()

    def move_to_element(self, element):
        return webdriver.ActionChains(self.browser).\
            move_to_element(element).perform()

    def one_click(self, value):
        webdriver.ActionChains(self.browser).click(value).perform()

    def right_click(self, value):
        webdriver.ActionChains(self.browser).context_click(value).perform()

    def select_all_text(self, element):     # triple click
        webdriver.ActionChains(self.browser).double_click(element).click().perform()
