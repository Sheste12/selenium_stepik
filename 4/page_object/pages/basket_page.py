from .base_page import BasePage
from .locators import BasketPageLocators

class BasketPage(BasePage):
    def should_not_have_products(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_PRODUCT_TABLE), \
            "Basket should not have any products"

    def should_have_empty_basket_message(self):
        assert self.is_element_present(*BasketPageLocators.BASKET_IS_EMPTY_MESSAGE), \
            "Basket should be have message that it's empty"
