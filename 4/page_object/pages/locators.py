from selenium.webdriver.common.by import By

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.CSS_SELECTOR, ".basket-mini > span > a.btn-default")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "a#registration_link")

class BasketPageLocators():
    BASKET_PRODUCT_TABLE = (By.CSS_SELECTOR, "#basket_formset")
    BASKET_IS_EMPTY_MESSAGE = (By.CSS_SELECTOR, ".content > #content_inner > p")

class LoginPageLocators():
    EMAIL_LOGIN = (By.CSS_SELECTOR, "#id_login-username")
    PASSWORD_LOGIN = (By.CSS_SELECTOR, "#id_login-password")
    BUTTON_LOGIN = (By.CSS_SELECTOR, ".btn-primary[name=login_submit]")

    EMAIL_REGISTRATION = (By.CSS_SELECTOR, "#id_registration-email")
    PASSWORD_REGISTRATION = (By.CSS_SELECTOR, "#id_registration-password1")
    PASSWORD_REGISTRATION_CONFIRM = (By.CSS_SELECTOR, "#id_registration-password2")
    REGISTRATION_BUTTON = (By.CSS_SELECTOR, ".btn-primary[name=registration_submit]")

class ProductPageLocators():
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main > h1")
    BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    ADD_TO_BASKET_PRODUCT_NAME = (By.CSS_SELECTOR, "#messages .alert:first-child .alertinner strong")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main > .price_color")
    PRODUCT_TOTAL = (By.CSS_SELECTOR, "#messages .alert:last-child .alertinner strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alert:first-child")