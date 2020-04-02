from .links import Links
from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage
from selenium.webdriver import Remote
import pytest

class TestLoginFromMainPage:
    @pytest.mark.xfail(reason="В текущей странице продукта отсутствует верная ссылка на страницу логина.")
    @pytest.mark.parametrize(*Links.THIRD_PRODUCT_PAGE)
    def test_guest_can_go_to_login_page(self, browser: Remote, link):
        page = MainPage(browser, link)
        page.open()
        page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_page()

    @pytest.mark.parametrize(*Links.MAIN_PAGE)
    def test_guest_cant_see_product_in_basket_opened_from_main_page(self, browser: Remote, link):
        page = MainPage(browser, link)
        page.open()
        page.go_to_basket()
        basket_page = BasketPage(browser, browser.current_url)
        basket_page.should_not_have_products()
        basket_page.should_have_empty_basket_message()
