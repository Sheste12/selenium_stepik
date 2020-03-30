from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def click_button_add_to_basket(self):
        product_name = self.get_element(ProductPageLocators.PRODUCT_NAME)
        header_name = product_name.text
        product_price = self.get_element(ProductPageLocators.PRODUCT_PRICE)
        product_price_value = product_price.text
        basket_btn = self.get_element(ProductPageLocators.BASKET_BUTTON)
        basket_btn.click()
        self.solve_quiz_and_get_code()
        add_to_basket_product_name = self.get_element(ProductPageLocators.ADD_TO_BASKET_PRODUCT_NAME)
        product_total = self.get_element(ProductPageLocators.PRODUCT_TOTAL)
        self.check_product_name(header_name, add_to_basket_product_name)
        self.check_price_with_basket_total(product_price_value, product_total)

    def check_if_page_has_not_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def check_if_page_has_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is not presented, but should be"

    def check_product_name(self, header_name, success_message_name_element):
        self.check_name(header_name, success_message_name_element.text)

    def check_price_with_basket_total(self, price_value, total_element):
        self.check_name(price_value, total_element.text)
