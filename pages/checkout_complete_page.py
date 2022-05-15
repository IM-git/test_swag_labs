from pages import BasePage
from locators import *


class CheckoutCompletePage(BasePage):

    def __init__(self, *args, **kwargs):
        super(CheckoutCompletePage, self).__init__(*args, **kwargs)

    def checks_is_displayed_button(self):
        self.check_is_displayed(*CheckoutComplete.BUTTON_BACK_HOME)

    def clicks_finish_button(self):
        self.click_element(*CheckoutComplete.BUTTON_BACK_HOME)

    def wait_is_clickable_button(self):
        self.wait_element_to_be_clickable(*CheckoutComplete.BUTTON_BACK_HOME,
                                          Base.TIME)
