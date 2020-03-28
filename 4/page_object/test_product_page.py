from .pages.product_page import ProductPage
from selenium.webdriver import Remote

def test_guest_can_add_product_to_basket(browser: Remote):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(browser, link)
    page.open()
    page.click_button_add_to_basket("The shellcoder's handbook")
