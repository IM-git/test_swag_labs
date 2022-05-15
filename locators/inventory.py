from selenium.webdriver.common.by import By


class Inventory:
    LINK = "https://www.saucedemo.com/inventory.html"
    IMG_ROBOT = (By.XPATH, "//img[@class='footer_robot']")
    BUTTON_BACKPACK = (By.XPATH, "//button[@id='add-to-cart-sauce-labs-backpack']")
    BUTTON_JACKET = (By.XPATH, "//button[@id='add-to-cart-sauce-labs-fleece-jacket']")
    BUTTON_CHECKOUT = (By.XPATH, "//button[@id='checkout']")
    SHOPPING_CARD_LINK = (By.XPATH, "//a[@class='shopping_cart_link']")
    SHOPPING_CARD_BADGE = (By.XPATH, "//span[@class='shopping_cart_badge']")

