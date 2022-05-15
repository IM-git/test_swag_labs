from pages import BasePage
from locators import *
from src.enums import *


class InventoryPage(BasePage):

    def __init__(self, *args, **kwargs):
        super(InventoryPage, self).__init__(*args, **kwargs)

    def checks_is_displayed_element_img_robot(self):
        self.check_is_displayed(*Inventory.IMG_ROBOT)

    def checks_is_displayed_element_number_of_purchases(self):
        self.check_is_displayed(*Inventory.SHOPPING_CARD_BADGE)

    def checks_is_displayed_element_checkout_buttons(self):
        self.check_is_displayed(*Inventory.BUTTON_CHECKOUT)

    def checks_number_of_purchases(self):
        value = self.get_text(*Inventory.SHOPPING_CARD_BADGE)
        assert int(value) == 2,\
            InventoryErrorMessages.WRONG_NUMBER_OF_PURCHASES.value

    def click_add_to_cart_backpack_button(self):
        self.click_element(*Inventory.BUTTON_BACKPACK)

    def click_shopping_cart_link_buttons(self):
        self.click_element(*Inventory.SHOPPING_CARD_LINK)

    def click_add_to_cart_jacket_button(self):
        self.click_element(*Inventory.BUTTON_JACKET)
