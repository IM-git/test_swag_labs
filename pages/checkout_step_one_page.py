from pages import BasePage
from locators import *


class CheckoutStepOnePage(BasePage):

    def __init__(self, *args, **kwargs):
        super(CheckoutStepOnePage, self).__init__(*args, **kwargs)

    def checks_is_displayed_input(self):
        self.check_is_displayed(*CheckoutStepOne.INPUT_CONTINUE)

    def click_continue_input(self):
        self.click_element(*CheckoutStepOne.INPUT_CONTINUE)

    def enter_first_name(self):
        self.enter_value(*CheckoutStepOne.INPUT_FIRST_NAME,
                         CheckoutStepOne.FIRST_NAME)

    def enter_last_name(self):
        self.enter_value(*CheckoutStepOne.INPUT_LAST_NAME,
                         CheckoutStepOne.LAST_NAME)

    def enter_zip_postal_code(self):
        self.enter_value(*CheckoutStepOne.INPUT_ZIP_POSTAL_CODE,
                         CheckoutStepOne.ZIP_POSTAL_CODE)

    def wait_is_clickable_input(self):
        self.wait_element_to_be_clickable(*CheckoutStepOne.INPUT_CONTINUE,
                                          Base.TIME)
