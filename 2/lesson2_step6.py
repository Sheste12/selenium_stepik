from selenium import webdriver
from selenium.webdriver.support.ui import Select
import tkinter
from tkinter import messagebox
import time
import traceback
import math

def test(link, n):
    try:
        # Открыть страницу http://SunInJuly.github.io/execute_script.html.
        browser = webdriver.Chrome()
        browser.get(link)
        # Считать значение для переменной x.
        x = browser.find_element_by_id("input_value").text
        # Посчитать математическую функцию от x.
        y = calc(x)
        # Проскроллить страницу вниз.
        browser.execute_script("window.scrollBy(0, 200);")
        # Ввести ответ в текстовое поле.
        answer = browser.find_element_by_id("answer")
        answer.send_keys(y)
        # Выбрать checkbox "I'm the robot".
        checkbox_robot = browser.find_element_by_id("robotCheckbox")
        checkbox_robot.click()
        # Переключить radiobutton "Robots rule!".
        radiobutton = browser.find_element_by_id("robotsRule")
        radiobutton.click()
        # Нажать на кнопку "Submit".
        btn = browser.find_element_by_css_selector("button.btn")
        btn.click()

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
    test("http://SunInJuly.github.io/execute_script.html", 'Lesson 2 Step 6')


if __name__ == '__main__':
    main()
