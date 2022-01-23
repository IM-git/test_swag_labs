import requests
import allure
from selenium.webdriver.common.by import By
import time

from pages import LoginPage
from pages import InventoryPage
from locators import Base
from locators import Login
from locators import Inventory
from src.enums import GlobalErrorMessages
from src.enums import LoginPageErrorMessages
from src.enums import InventoryErrorMessages
from tools import Logger
from tools import AllureScreenshot
from tools import RandomName


@allure.feature("Main page.")
@allure.link(url=Base.LINK, name='BASE_LINK')
# @Logger.logger.catch()
def test_standard_steps(browser):
    login_page = LoginPage()
    inventory_page = InventoryPage()
    page_response = requests.get(url=Base.LINK)
    open_login_page = login_page.open_page(browser, Base.LINK)
    check_is_displayed_element_img = login_page.check_is_displayed(
        browser, By.XPATH, Login.ELEMENT_IMG)
    wait_is_clickable_button = login_page.wait_element_to_be_clickable(
        browser, By.XPATH, Login.BUTTON)
    enter_username = login_page.enter_value(
        browser, By.XPATH, Login.USERNAME_FIELD, Login.LIST_NAMES[0])
    enter_password = login_page.enter_value(
        browser, By.XPATH, Login.PASSWORD_FIELD, Login.PASSWORD)
    click_login_button = login_page.click_element(
        browser, By.XPATH, Login.BUTTON)
    
    get_current_url = login_page.get_url(browser)
    check_is_displayed_element_img_robot = login_page.check_is_displayed(
        browser, By.XPATH, Inventory.IMG_ROBOT)
    page_response_with_inventory = requests.get(url=get_current_url)
    click_add_to_cart_backpack_button = inventory_page.click_element(
        browser, By.XPATH, Inventory.BUTTON_BACKPACK)
    click_add_to_cart_jacket_button = inventory_page.click_element(
        browser, By.XPATH, Inventory.BUTTON_JACKET)
    check_is_displayed_element_number_of_purchases =\
        inventory_page.check_is_displayed(
            browser, By.XPATH, Inventory.SHOPPING_CARD_BADGE)
    get_number_of_purchases = inventory_page.get_text(
        browser, By.XPATH, Inventory.SHOPPING_CARD_BADGE)
    click_shopping_cart_link_buttons = ''

    assert page_response.status_code == 200, \
        GlobalErrorMessages.WRONG_STATUS_CODE.value
    assert page_response_with_inventory.status_code == 404, \
        GlobalErrorMessages.WRONG_STATUS_CODE.value
    assert Inventory.LINK == get_current_url, \
        LoginPageErrorMessages.WRONG_PAGE.value
    assert check_is_displayed_element_number_of_purchases is True,\
        InventoryErrorMessages.WRONG_DISPLAYED.value
    assert get_number_of_purchases == 2,\
        InventoryErrorMessages.WRONG_NUMBER_OF_PURCHASES.value

    taking_screenshot = AllureScreenshot().make_screenshot(browser)
