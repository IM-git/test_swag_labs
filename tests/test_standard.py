import requests
import allure
from selenium.webdriver.common.by import By
import time

from pages import *
from locators import *
from src.enums import *
from tools import logger as Logger
from tools.allure_screenshot import taking_screenshot
from tools import AllureScreenshot


@allure.feature("Main pages.")
@allure.link(url=Login.LINK, name='LOGIN_LINK')
@Logger.logger.catch()
def test_standard_steps(browser):
    """Log in to the site. Chose two things to buy.
    Checking the number of items in the trading card icon.
    Checking the things we have chosen. Entered first name,
    last name, zip/postal code.
    Expect that the purchase was completed correctly."""
    login_page = LoginPage()
    inventory_page = InventoryPage()
    checkout_step_one_page = CheckoutStepOnePage()
    checkout_step_two_page = CheckoutStepTwoPage()
    checkout_complete_page = CheckoutCompletePage()

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
    taking_screenshot(browser)
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
    taking_screenshot(browser)
    click_shopping_cart_link_buttons = inventory_page.click_element(
        browser, By.XPATH, Inventory.SHOPPING_CARD_LINK)

    check_is_displayed_element_checkout_buttons = \
        inventory_page.check_is_displayed(
            browser, By.XPATH, Inventory.BUTTON_CHECKOUT)
    wait_is_clickable_button = \
        checkout_step_two_page.wait_element_to_be_clickable(
            browser, By.XPATH, Inventory.BUTTON_CHECKOUT)
    get_current_url_on_inventory_page = \
        checkout_step_two_page.get_url(browser)
    page_response_with_inventory_page = requests.get(
        url=get_current_url_on_inventory_page)
    taking_screenshot(browser)
    click_checkout_buttons = inventory_page.click_element(
        browser, By.XPATH, Inventory.BUTTON_CHECKOUT)

    check_is_displayed_input = checkout_step_one_page.check_is_displayed(
        browser, By.XPATH, CheckoutStepOne.INPUT_CONTINUE)
    wait_is_clickable_input = \
        checkout_step_one_page.wait_element_to_be_clickable(
            browser, By.XPATH, CheckoutStepOne.INPUT_CONTINUE)
    get_current_url_on_checkout_step_one = \
        checkout_step_one_page.get_url(browser)
    page_response_with_checkout_step_one = requests.get(
        url=get_current_url_on_checkout_step_one)
    enter_first_name = checkout_step_one_page.enter_value(
        browser, By.XPATH, CheckoutStepOne.INPUT_FIRST_NAME,
        CheckoutStepOne.FIRST_NAME)
    enter_last_name = checkout_step_one_page.enter_value(
        browser, By.XPATH, CheckoutStepOne.INPUT_LAST_NAME,
        CheckoutStepOne.LAST_NAME)
    enter_zip_postal_code = checkout_step_one_page.enter_value(
        browser, By.XPATH, CheckoutStepOne.INPUT_ZIP_POSTAL_CODE,
        CheckoutStepOne.ZIP_POSTAL_CODE)
    taking_screenshot(browser)
    click_continue_input = checkout_step_one_page.click_element(
        browser, By.XPATH, CheckoutStepOne.INPUT_CONTINUE)

    check_is_displayed_button = checkout_step_two_page.check_is_displayed(
        browser, By.XPATH, CheckoutStepTwo.BUTTON_FINISH)
    wait_is_clickable_button = \
        checkout_step_two_page.wait_element_to_be_clickable(
            browser, By.XPATH, CheckoutStepTwo.BUTTON_FINISH)
    get_current_url_on_checkout_step_two = \
        checkout_step_two_page.get_url(browser)
    page_response_with_checkout_step_two = requests.get(
        url=get_current_url_on_checkout_step_two)
    taking_screenshot(browser)
    click_finish_button = checkout_step_two_page.click_element(
        browser, By.XPATH, CheckoutStepTwo.BUTTON_FINISH)

    check_is_displayed_button = checkout_complete_page.check_is_displayed(
        browser, By.XPATH, CheckoutComplete.BUTTON_BACK_HOME)
    wait_is_clickable_button = \
        checkout_complete_page.wait_element_to_be_clickable(
            browser, By.XPATH, CheckoutComplete.BUTTON_BACK_HOME)
    get_current_url_on_checkout_complete = \
        checkout_complete_page.get_url(browser)
    page_response_with_checkout_complete = requests.get(
        url=get_current_url_on_checkout_complete)
    taking_screenshot(browser)
    click_finish_button = checkout_complete_page.click_element(
        browser, By.XPATH, CheckoutComplete.BUTTON_BACK_HOME)
    taking_screenshot(browser)

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

    assert page_response_with_checkout_step_one.status_code == 404, \
        GlobalErrorMessages.WRONG_STATUS_CODE.value
    assert CheckoutStepOne.LINK == get_current_url_on_checkout_step_one, \
        CheckoutStepOneErrorMessages.WRONG_PAGE.value

    assert page_response_with_checkout_step_two.status_code == 404, \
        GlobalErrorMessages.WRONG_STATUS_CODE.value
    assert CheckoutStepTwo.LINK == get_current_url_on_checkout_step_two, \
        CheckoutStepTwoErrorMessages.WRONG_PAGE.value

    assert page_response_with_checkout_complete.status_code == 404, \
        GlobalErrorMessages.WRONG_STATUS_CODE.value
    assert CheckoutComplete.LINK == get_current_url_on_checkout_complete, \
        CheckoutCompleteErrorMessages.WRONG_PAGE.value


# def foo():
#     check_is_displayed_element_checkout_buttons = \
#         inventory_page.check_is_displayed(
#             browser, By.XPATH, Inventory.BUTTON_CHECKOUT)
#     wait_is_clickable_button = \
#         checkout_step_two_page.wait_element_to_be_clickable(
#             browser, By.XPATH, Inventory.BUTTON_CHECKOUT)
#     get_current_url_on_inventory_page = \
#         checkout_step_two_page.get_url(browser)
#     page_response_with_inventory_page = requests.get(
#         url=get_current_url_on_inventory_page)
#     taking_screenshot(browser)
#     click_checkout_buttons = inventory_page.click_element(
#         browser, By.XPATH, Inventory.BUTTON_CHECKOUT)
