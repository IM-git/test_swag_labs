import requests
import allure
from pages import BasePage
from selenium.webdriver.common.by import By
from locators.base import Base
from src.enums import GlobalErrorMessages
from tools import logger
from tools.allure_screenshot import AllureScreenshot


@allure.feature("Main page.")
@allure.link(url=Base.LINK, name='BASE_LINK')
# @logger.logger.catch()
def test_main_page(browser):
    base_page = BasePage()
    page_response = requests.get(url=Base.LINK)
    open_site_saucedemo = base_page.open_page(browser, Base.LINK)
    check_is_displayed_element_img = base_page.check_is_displayed(
        browser, By.XPATH, Base.ELEMENT_IMG)
    wait_is_clickable_button = base_page.wait_element_to_be_clickable(
        browser, By.XPATH, Base.BUTTON)

    assert page_response.status_code == 200, \
        GlobalErrorMessages.WRONG_STATUS_CODE.value

    taking_screenshot = AllureScreenshot().make_screenshot(browser)
