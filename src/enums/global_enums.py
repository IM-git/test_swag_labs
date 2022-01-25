from enum import Enum


# MESSAGES FOR ASSERTS IN TEST FILES

class GlobalErrorMessages(Enum):
    WRONG_STATUS_CODE = 'Received status code is not equal to expected!!'
    WRONG_TITLE_PAGE = 'Another page is open!!'
    WRONG_IS_DISPLAYED = 'The page is not loaded!!'


class LoginPageErrorMessages(Enum):
    WRONG_PAGE = 'This is other page, right link: https://www.saucedemo.com/inventory.html'
    LOGIN_COOKIE = 'Cookies should not be!!'
    MISMATCH = 'Value is not match!!'


class InventoryErrorMessages(Enum):
    WRONG_DISPLAYED = "The element isn't displayed!!"
    WRONG_NUMBER_OF_PURCHASES = 'The number of purchases must be equals: 2!!'


class CheckoutStepOneErrorMessages(Enum):
    WRONG_PAGE = 'This is other page, right link: https://www.saucedemo.com/checkout-step-one.html'


class CheckoutStepTwoErrorMessages(Enum):
    WRONG_PAGE = 'This is other page, right link: https://www.saucedemo.com/checkout-step-two.html'


class CheckoutCompleteErrorMessages(Enum):
    WRONG_PAGE = 'This is other page, right link: https://www.saucedemo.com/checkout-complete.html'
