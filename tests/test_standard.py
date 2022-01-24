import requests
import allure
from selenium.webdriver.common.by import By
import time

from pages import LoginPage
from pages import InventoryPage
from pages import CheckoutStepOnePage
from locators import Base
from locators import Login
from locators import Inventory
from locators import CheckoutStepOne
from src.enums import GlobalErrorMessages
from src.enums import LoginPageErrorMessages
from src.enums import InventoryErrorMessages
from tools import Logger
from tools import AllureScreenshot


@allure.feature("Main page.")
@allure.link(url=Base.LINK, name='BASE_LINK')
# @Logger.logger.catch()
def test_standard_steps(browser):
    login_page = LoginPage()
    inventory_page = InventoryPage()
    checkout_step_one_page = CheckoutStepOnePage()
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
    
    check_is_displayed_element_img_robot = inventory_page.check_is_displayed(
        browser, By.XPATH, Inventory.IMG_ROBOT)
    get_current_url = inventory_page.get_url(browser)
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
    click_shopping_cart_link_buttons = inventory_page.click_element(
        browser, By.XPATH, Inventory.SHOPPING_CARD_LINK)
    check_is_displayed_element_checkout_buttons = \
        inventory_page.check_is_displayed(
            browser, By.XPATH, Inventory.BUTTON_CHECKOUT)
    click_checkout_buttons = inventory_page.click_element(
        browser, By.XPATH, Inventory.BUTTON_CHECKOUT)

    check_is_displayed_element_continue = checkout_step_one_page.check_is_displayed(
        browser, By.XPATH, CheckoutStepOne.INPUT_CONTINUE)
    wait_is_clickable_button = login_page.wait_element_to_be_clickable(
        browser, By.XPATH, CheckoutStepOne.INPUT_CONTINUE)
    get_current_url_2 = checkout_step_one_page.get_url(browser)
    page_response_with_checkout = requests.get(url=get_current_url_2)
    enter_first_name = checkout_step_one_page.enter_value(
        browser, By.XPATH, CheckoutStepOne.INPUT_FIRST_NAME,
        CheckoutStepOne.FIRST_NAME)
    enter_last_name = checkout_step_one_page.enter_value(
        browser, By.XPATH, CheckoutStepOne.INPUT_LAST_NAME,
        CheckoutStepOne.LAST_NAME)
    enter_zip_postal_code = checkout_step_one_page.enter_value(
        browser, By.XPATH, CheckoutStepOne.INPUT_ZIP_POSTAL_CODE,
        CheckoutStepOne.ZIP_POSTAL_CODE)
    click_continue_button = checkout_step_one_page.click_element(
        browser, By.XPATH, CheckoutStepOne.INPUT_CONTINUE)

    time.sleep(3)

    assert page_response.status_code == 200, \
        GlobalErrorMessages.WRONG_STATUS_CODE.value
    assert page_response_with_inventory.status_code == 404, \
        GlobalErrorMessages.WRONG_STATUS_CODE.value
    assert Inventory.LINK == get_current_url, \
        LoginPageErrorMessages.WRONG_PAGE.value
    assert check_is_displayed_element_number_of_purchases is True,\
        InventoryErrorMessages.WRONG_DISPLAYED.value
    assert int(get_number_of_purchases) == 2,\
        InventoryErrorMessages.WRONG_NUMBER_OF_PURCHASES.value
    assert page_response_with_checkout.status_code == 404, \
        GlobalErrorMessages.WRONG_STATUS_CODE.value
    assert Inventory.LINK == get_current_url, \
        LoginPageErrorMessages.WRONG_PAGE.value

    taking_screenshot = AllureScreenshot().make_screenshot(browser)
