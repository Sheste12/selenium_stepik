from .pages.product_page import ProductPage
from .pages.basket_page import BasketPage
from selenium.webdriver import Remote
import pytest

@pytest.mark.skip()
@pytest.mark.parametrize(
    'link',
    [
    # "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
    # "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
    # "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
    # "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
    # "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
    # "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
    # "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
    # pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7", marks=pytest.mark.xfail),
    # "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"
])
class TestProductPage:
    @pytest.mark.skip(reason="test_guest_can_add_product_to_basket")
    def test_guest_can_add_product_to_basket(self, browser: Remote, link):
        page = ProductPage(browser, link)
        page.open()
        page.click_button_add_to_basket()

    def test_guest_cant_see_success_message_after_adding_product_to_basket(sefl, browser : Remote, link):
        page = ProductPage(browser, link, 0)
        page.open()
        page.click_button_add_to_basket()
        # time.sleep(60)
        page.check_if_page_has_not_success_message()


    def test_guest_cant_see_success_message(self, browser : Remote, link):
        page = ProductPage(browser, link, 0)
        page.open()
        page.check_if_page_has_not_success_message()

    def test_message_disappeared_after_adding_product_to_basket(self, browser : Remote, link):
        page = ProductPage(browser, link, 0)
        page.open()
        page.click_button_add_to_basket()
        page.check_if_page_has_success_message()

@pytest.mark.skip()
def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

@pytest.mark.skip()
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()

def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_basket()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_not_have_products()
    basket_page.should_have_empty_basket_message()