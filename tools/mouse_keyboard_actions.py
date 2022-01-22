from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class MouseKeyboardActions:

    def _move_to_element(self, browser, element):
        return webdriver.ActionChains(browser).\
            move_to_element(element).perform()

    def _one_click(self, browser, value):
        return webdriver.ActionChains(browser).\
            click(value).perform()

    def _double_click(self, browser, value):
        return webdriver.ActionChains(browser).\
            double_click(value).perform()

    def _right_click(self, browser, value):
        return webdriver.ActionChains(browser).\
            context_click(value).perform()

    def _select_all_text(self, browser, element):     # triple click
        return webdriver.ActionChains(browser).\
            double_click(element).click().perform()

    def _enter_text(self, browser, text):
        return webdriver.ActionChains(browser).send_keys(text).perform()

    def _delete_text(self, browser, element):
        return element.send_keys(Keys.DELETE)

    def _click_arrow_up(self, browser):
        return webdriver.ActionChains(browser).send_keys(Keys.ARROW_UP)

    def _click_arrow_down(self, browser):
        return webdriver.ActionChains(browser).\
            send_keys(Keys.ARROW_DOWN).perform()

    def _click_enter(self, browser):
        return webdriver.ActionChains(browser).\
            send_keys(Keys.ENTER).perform()

    def _click_tab(self, browser):
        return webdriver.ActionChains(browser).\
            send_keys(Keys.TAB).perform()

    def _do_key_down(self, browser):
        return webdriver.ActionChains(browser).key_down(Keys.SHIFT)

    def _perform(self, browser, value):
        return value.perform()
