from selenium import webdriver
from tkinter import messagebox
import tkinter
import time
import traceback
import unittest

class TestStepik(unittest.TestCase):
    def test_n1(self):
        browser = webdriver.Chrome()
        browser.get("http://suninjuly.github.io/registration1.html")

        input1 = browser.find_element_by_css_selector(".first_block .first_class input")
        input1.send_keys("Ivan")
        input2 = browser.find_element_by_css_selector(".first_block .second_class input")
        input2.send_keys("Ivanov")
        input3 = browser.find_element_by_css_selector(".first_block .third_class input")
        input3.send_keys("ivan@ivanov.com")
        input4 = browser.find_element_by_css_selector(".second_block .first_class input")
        input4.send_keys("+7 999 999 99")
        input5 = browser.find_element_by_css_selector(".second_block .second_class input")
        input5.send_keys("Moscow, Red Square")

        button = browser.find_element_by_css_selector("button.btn")
        button.click()

        time.sleep(1)

        welcome_text_elt = browser.find_element_by_tag_name("h1")
        welcome_text = welcome_text_elt.text

        self.assertEqual("Congratulations! You have successfully registered!", welcome_text, "Should be successful message")
        time.sleep(10)
        browser.quit()

    def test_n2(self):
        browser = webdriver.Chrome()
        browser.get("http://suninjuly.github.io/registration2.html")

        input1 = browser.find_element_by_css_selector(".first_block .first_class input")
        input1.send_keys("Ivan")
        input2 = browser.find_element_by_css_selector(".first_block .second_class input")
        input2.send_keys("Ivanov")
        input3 = browser.find_element_by_css_selector(".first_block .third_class input")
        input3.send_keys("ivan@ivanov.com")
        input4 = browser.find_element_by_css_selector(".second_block .first_class input")
        input4.send_keys("+7 999 999 99")
        input5 = browser.find_element_by_css_selector(".second_block .second_class input")
        input5.send_keys("Moscow, Red Square")

        button = browser.find_element_by_css_selector("button.btn")
        button.click()

        time.sleep(1)

        welcome_text_elt = browser.find_element_by_tag_name("h1")
        welcome_text = welcome_text_elt.text

        self.assertEqual("Congratulations! You have successfully registered!", welcome_text, "Should be successful message")
        time.sleep(10)
        browser.quit()

def main():
    root = tkinter.Tk()
    root.withdraw()
    unittest.main()

if __name__ == '__main__':
    main()
