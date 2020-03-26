from selenium import webdriver
from tkinter import messagebox
import time
import traceback

def test(link, n):
    try:
        browser = webdriver.Chrome()
        browser.get(link)

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

        assert "Congratulations! You have successfully registered!" == welcome_text

        success_msg(n)
    except Exception as e:
        error_msg(n, traceback.format_exc())
    finally:
        time.sleep(10)
        browser.quit()

def success_msg(n):
    messagebox.showinfo(f"Test {n}", f"Test {n} is successful!")

def error_msg(n, er_txt):
    messagebox.showerror(f"Test {n}", f"Test {n} is not successful!\n{er_txt}")

def main():
    test("http://suninjuly.github.io/registration1.html", 1)
    test("http://suninjuly.github.io/registration2.html", 2)

if __name__ == '__main__':
    main()
