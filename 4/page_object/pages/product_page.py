from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def click_button_add_to_basket(self, product_name):
        self.check_product_name(product_name, ProductPageLocators.PRODUCT_NAME)
        self.basket_button_is_presented()
        btn_basket = self.browser.find_element(*ProductPageLocators.BASKET_BUTTON)
        btn_basket.click()
        self.solve_quiz_and_get_code()
        self.check_product_name(product_name, ProductPageLocators.ADD_TO_BASKET_PRODUCT_NAME)
        self.check_price_with_basket_total(ProductPageLocators.PRODUCT_PRICE, ProductPageLocators.PRODUCT_TOTAL)

    def basket_button_is_presented(self):
        assert self.is_element_present(*ProductPageLocators.BASKET_BUTTON), \
            "Basket button is not presented"

    def check_product_name(self, name, css_selector):
        assert self.is_element_present(*css_selector), \
            f"{name} selector is not presented"
        product_name = self.browser.find_element(*css_selector).text
        assert name == product_name, \
            f"Name product should be {name} instead {product_name}"

    def check_price_with_basket_total(self, price_css_selector, total_css_selector):
        assert self.is_element_present(*price_css_selector), \
            f"Price selector is not presented"
        assert self.is_element_present(*total_css_selector), \
            f"Total selector is not presented"
        price_value = self.browser.find_element(*price_css_selector).text
        total_value = self.browser.find_element(*total_css_selector).text
        assert price_value == total_value, \
            f"Total value should be {price_value} instead of {total_value}"