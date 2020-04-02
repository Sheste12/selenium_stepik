# Все ссылки на странице находятся в отдельном конфиге links.py
from .links import Links
from .pages.product_page import ProductPage
from .pages.basket_page import BasketPage
from .pages.login_page import LoginPage
from selenium.webdriver import Remote
import pytest
import time

@pytest.mark.parametrize(*Links.PRODUCT_PAGES)
class TestProductPage:
    @pytest.mark.need_review
    def test_guest_can_add_product_to_basket(self, browser: Remote, link):
        page = ProductPage(browser, link)
        page.open()
        page.click_button_add_to_basket()

    @pytest.mark.xfail(reason="Пользователь должен видеть сообщение об успехе после добавления в корзину.")
    def test_guest_cant_see_success_message_after_adding_product_to_basket(self, browser: Remote, link):
        page = ProductPage(browser, link, 0)
        page.open()
        page.click_button_add_to_basket()
        page.check_if_page_has_not_success_message()

    def test_guest_cant_see_success_message(self, browser: Remote, link):
        page = ProductPage(browser, link)
        page.open()
        page.check_if_page_has_not_success_message()

    @pytest.mark.xfail(reason="Сообщение об успехе не пропадает после добавления в корзину.")
    def test_message_disappeared_after_adding_product_to_basket(self, browser: Remote, link):
        page = ProductPage(browser, link)
        page.open()
        page.click_button_add_to_basket()
        page.check_if_page_has_success_message()

@pytest.mark.parametrize(*Links.FIRST_PRODUCT_PAGE)
@pytest.mark.parametrize(*Links.LOGIN_PAGE)
class TestUserAddToBasketFromProductPage:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser: Remote, login_page_link):
        page = LoginPage(browser, login_page_link)
        page.open()
        page.should_be_login_page()
        email = str(time.time()) + "@fakemail.org"
        password = "password_for_testing13"
        page.register_new_user(email, password)

    def test_user_cant_see_success_message(self, browser: Remote, link):
        page = ProductPage(browser, link)
        page.open()
        page.check_if_page_has_not_success_message()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser: Remote, link):
        page = ProductPage(browser, link)
        page.open()
        page.click_button_add_to_basket()

@pytest.mark.parametrize(*Links.SECOND_PRODUCT_PAGE)
class TestLoginPageFromProductPage:
    def test_guest_should_see_login_link_on_product_page(self, browser: Remote, link):
        page = ProductPage(browser, link)
        page.open()
        page.should_be_login_link()

    @pytest.mark.need_review
    def test_guest_can_go_to_login_page_from_product_page(self, browser: Remote, link):
        page = ProductPage(browser, link)
        page.open()
        page.go_to_login_page()

    @pytest.mark.need_review
    def test_guest_cant_see_product_in_basket_opened_from_product_page(self, browser: Remote, link):
        page = ProductPage(browser, link)
        page.open()
        page.go_to_basket()
        basket_page = BasketPage(browser, browser.current_url)
        basket_page.should_not_have_products()
        basket_page.should_have_empty_basket_message()