from .pages.main_page import MainPage
from .pages.login_page import LoginPage

def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209?promo=midsummer"
    page = MainPage(browser, link)
    page.open()
    page.should_be_login_link()
    page.go_to_login_page()
    login_link = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"
    login_page = LoginPage(browser, login_link)
    login_page.open()
    login_page.should_be_login_page()