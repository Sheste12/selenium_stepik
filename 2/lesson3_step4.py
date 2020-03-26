from selenium import webdriver
import tkinter
from tkinter import messagebox
import time
import traceback
import math

def test(link, n):
    try:
        # Открыть страницу http://suninjuly.github.io/alert_accept.html
        browser = webdriver.Chrome()
        browser.get(link)
        # Нажать на кнопку
        btn = browser.find_element_by_css_selector("button.btn.btn-primary")
        btn.click()
        # Принять confirm
        confirm = browser.switch_to.alert
        confirm.accept()
        # На новой странице решить капчу для роботов, чтобы получить число с ответом
        x = browser.find_element_by_id("input_value").text
        y = calc(x)

        answer = browser.find_element_by_id("answer")
        answer.send_keys(y)

        submit = browser.find_element_by_css_selector("button.btn.btn-primary")
        submit.click()

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

def calc(x):
    return str( math.log( abs( 12 * math.sin( int(x) ) ) ) )

def main():
    root = tkinter.Tk()
    root.withdraw()
    test("http://suninjuly.github.io/alert_accept.html", 'Lesson 3 Step 4')


if __name__ == '__main__':
    main()
