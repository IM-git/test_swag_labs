from selenium.webdriver.common.by import By


class CheckoutStepTwo:
    LINK = "https://www.saucedemo.com/checkout-step-two.html"
    BUTTON_FINISH = (By.XPATH, "//button[@id='finish']")
