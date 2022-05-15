from selenium.webdriver.common.by import By


class CheckoutComplete:
    LINK = "https://www.saucedemo.com/checkout-complete.html"
    BUTTON_BACK_HOME = (By.XPATH, "//button[@id='back-to-products']")
