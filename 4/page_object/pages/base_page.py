from selenium.webdriver import Remote
from selenium.common.exceptions import *
from selenium.webdriver.support.ui import WebDriverWait as WDW
from selenium.webdriver.support import expected_conditions as EC
from .locators import BasePageLocators
import math

class BasePage():
    def __init__(self, browser : Remote, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        self.browser.get(self.url)

    def should_be_authorized_user(self):
        assert self.is_element_present(*BasePageLocators.USER_ICON), \
            "User icon is not presented, probably unauthorised user"

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True

    def is_not_element_present(self, how, what, timeout=4):
        try:
            WDW(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True
        return False

    def should_not_be_success_message(self, element):
        assert self.is_not_element_present(*element), \
            "Success message is presented, but should not be"

    def is_disappeared(self, how, what, timeout=4):
        try:
            WDW(self.browser, timeout, 1, TimeoutException)\
                .until_not(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False
        return True

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")

    def get_element(self, element):
        assert self.is_element_present(*element), \
            f"{element[1]} is not presented!"
        return self.browser.find_element(*element)

    @staticmethod
    def check_name(first_element_name, second_element_name):
        assert first_element_name == second_element_name, \
            f"The correct name should be {first_element_name} instead of {second_element_name}."

    def go_to_login_page(self):
        link = self.get_element(BasePageLocators.LOGIN_LINK)
        link.click()

    def should_be_login_link(self):
        assert self.is_element_present(*BasePageLocators.LOGIN_LINK), "Login link is not presented"

    def go_to_basket(self):
        btn = self.get_element(BasePageLocators.BASKET_LINK)
        btn.click()