from .base_page import BasePage
from .locators import LoginPageLocators

class LoginPage(BasePage):
    def register_new_user(self, email, password):
        self.go_to_login_page()
        self.should_be_register_form()
        email_registraion = self.get_element(LoginPageLocators.EMAIL_REGISTRATION)
        email_registraion.send_keys(email)
        password_registration = self.get_element(LoginPageLocators.PASSWORD_REGISTRATION)
        password_registration_confirm = self.get_element(LoginPageLocators.PASSWORD_REGISTRATION_CONFIRM)
        for p in (password_registration, password_registration_confirm):
            p.send_keys(password)
        btn = self.get_element(LoginPageLocators.REGISTRATION_BUTTON)
        btn.click()
        self.should_be_authorized_user()

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        current_url = self.browser.current_url
        assert "login" in current_url, \
            "Should be login URL."

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.EMAIL_LOGIN), \
            "Email in login form is not presented."
        assert self.is_element_present(*LoginPageLocators.PASSWORD_LOGIN), \
            "Password in login form is not presented."
        assert self.is_element_present(*LoginPageLocators.BUTTON_LOGIN), \
            "Login button in login form is not presented."

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.EMAIL_REGISTRATION), \
            "Email in registration form is not presented."
        assert self.is_element_present(*LoginPageLocators.PASSWORD_REGISTRATION), \
            "Password in registration form is not presented."
        assert self.is_element_present(*LoginPageLocators.PASSWORD_REGISTRATION_CONFIRM), \
            "Password confirm in registration form is not presented."
