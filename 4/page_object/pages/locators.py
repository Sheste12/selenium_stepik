from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "a#registration_link")

class LoginPageLocators():
    EMAIL_LOGIN = (By.CSS_SELECTOR, "#id_login-username")
    PASSWORD_LOGIN = (By.CSS_SELECTOR, "#id_login-password")
    BUTTON_LOGIN = (By.CSS_SELECTOR, ".btn-primary[name=login_submit]")

    EMAIL_REGISTRATION = (By.CSS_SELECTOR, "#id_registration-email")
    PASSWORD_REGISTRATION = (By.CSS_SELECTOR, "#id_registration-password1")
    PASSWORD_REGISTRATION_CONFIRM = (By.CSS_SELECTOR, ".btn-primary[name=registration_submit]")

class ProductPageLocators():
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main > h1")
    BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    ADD_TO_BASKET_PRODUCT_NAME = (By.CSS_SELECTOR, "#messages .alert:first-child .alertinner strong")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main > .price_color")
    PRODUCT_TOTAL = (By.CSS_SELECTOR, "#messages .alert:last-child .alertinner strong")