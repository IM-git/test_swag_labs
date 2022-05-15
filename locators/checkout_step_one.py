from selenium.webdriver.common.by import By


class CheckoutStepOne:
    LINK = "https://www.saucedemo.com/checkout-step-one.html"
    INPUT_CONTINUE = (By.XPATH, "//input[@id='continue']")
    INPUT_FIRST_NAME = (By.XPATH, "//input[@id='first-name']")
    INPUT_LAST_NAME = (By.XPATH, "//input[@id='last-name']")
    INPUT_ZIP_POSTAL_CODE = (By.XPATH, "//input[@id='postal-code']")
    FIRST_NAME = "Adam"
    LAST_NAME = "Adamov"
    ZIP_POSTAL_CODE = "000000"
