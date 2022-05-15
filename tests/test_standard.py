import allure

from pages import LoginPage
from pages import InventoryPage
from pages import CheckoutStepOnePage
from pages import CheckoutStepTwoPage
from pages import CheckoutCompletePage

from locators import *

from tools import logger as Logger


@allure.feature("Main pages.")
@allure.link(url=Login.LINK, name='LOGIN_LINK')
# @Logger.logger.catch()
def test_standard_steps(browser):
    """
    Log in to the site. Chose two things to buy.
    Checking the number of items in the trading card icon.
    Checking the things we have chosen. Entered first name,
    last name, zip/postal code.
    Expect that the purchase was completed correctly.
    """

    login_page = LoginPage(browser=browser, url=Base.LINK)
    inventory_page = InventoryPage(browser=browser, url=Inventory.LINK)
    checkout_step_one_page = CheckoutStepOnePage(browser=browser, url=CheckoutStepOne.LINK)
    checkout_step_two_page = CheckoutStepTwoPage(browser=browser, url=CheckoutStepTwo.LINK)
    checkout_complete_page = CheckoutCompletePage(browser=browser, url=CheckoutComplete.LINK)

    login_page.page_response()
    login_page.open_page()
    login_page.checks_is_displayed_element_img()
    login_page.wait_is_clickable_button()
    login_page.enter_username()
    login_page.enter_password()
    login_page.click_login_button()
    
    inventory_page.checks_is_displayed_element_img_robot()
    inventory_page.checks_page_response_404()
    inventory_page.click_add_to_cart_backpack_button()
    inventory_page.click_add_to_cart_jacket_button()
    inventory_page.checks_is_displayed_element_number_of_purchases()
    inventory_page.checks_number_of_purchases()
    inventory_page.click_shopping_cart_link_buttons()
    inventory_page.checks_is_displayed_element_checkout_buttons()

    checkout_step_two_page.wait_is_clickable_button_checkout()
    checkout_step_two_page.click_checkout_buttons()

    checkout_step_one_page.checks_is_displayed_input()
    checkout_step_one_page.wait_is_clickable_input()
    checkout_step_one_page.checks_page_response_404()
    checkout_step_one_page.enter_first_name()
    checkout_step_one_page.enter_last_name()
    checkout_step_one_page.enter_zip_postal_code()
    checkout_step_one_page.click_continue_input()

    checkout_step_two_page.checks_is_displayed_button()
    checkout_step_two_page.wait_is_clickable_button_finish()
    checkout_step_two_page.checks_page_response_404()
    checkout_step_two_page.click_finish_button()

    checkout_complete_page.checks_is_displayed_button()
    checkout_complete_page.wait_is_clickable_button()
    checkout_complete_page.checks_page_response_404()
    checkout_complete_page.clicks_finish_button()

