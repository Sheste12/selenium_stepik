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