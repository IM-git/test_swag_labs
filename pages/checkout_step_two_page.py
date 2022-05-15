from pages import BasePage
from locators import *


class CheckoutStepTwoPage(BasePage):

    def __init__(self, *args, **kwargs):
        super(CheckoutStepTwoPage, self).__init__(*args, **kwargs)

    def checks_is_displayed_button(self):
        self.check_is_displayed(*CheckoutStepTwo.BUTTON_FINISH)

    def click_checkout_buttons(self):
        self.click_element(*Inventory.BUTTON_CHECKOUT)

    def click_finish_button(self):
        self.click_element(*CheckoutStepTwo.BUTTON_FINISH)

    def wait_is_clickable_button_checkout(self):
        self.wait_element_to_be_clickable(*Inventory.BUTTON_CHECKOUT,
                                          Base.TIME)

    def wait_is_clickable_button_finish(self):
        self.wait_element_to_be_clickable(*CheckoutStepTwo.BUTTON_FINISH,
                                          Base.TIME)
