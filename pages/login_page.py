from pages import BasePage
from locators import *


class LoginPage(BasePage):

    def __init__(self, *args, **kwargs):
        super(LoginPage, self).__init__(*args, **kwargs)

    def checks_is_displayed_element_img(self):
        self.check_is_displayed(*Login.ELEMENT_IMG)

    def click_login_button(self):
        self.click_element(*Login.BUTTON)

    def enter_username(self):
        self.enter_value(*Login.USERNAME_FIELD, Login.LIST_NAMES[0])

    def enter_password(self):
        self.enter_value(*Login.PASSWORD_FIELD, Login.PASSWORD)

    def wait_is_clickable_button(self):
        self.wait_element_to_be_clickable(*Login.BUTTON, Base.TIME)
