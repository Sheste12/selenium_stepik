from selenium import webdriver
from tkinter import messagebox
import time
import traceback
import math

def test(link, n):
    try:
        # Открыть страницу http://suninjuly.github.io/math.html.
        browser = webdriver.Chrome()
        browser.get(link)
        # Считать значение для переменной x.
        x_element = browser.find_element_by_id("input_value")
        x = x_element.text
        # Посчитать математическую функцию от x (код для этого приведён ниже).
        y = calc(x)
        # Ввести ответ в текстовое поле.
        answer_input = browser.find_element_by_id("answer")
        answer_input.send_keys(y)
        # Отметить checkbox "I'm the robot".
        checkbox_robot = browser.find_element_by_id("robotCheckbox")
        checkbox_robot.click()
        # Выбрать radiobutton "Robots rule!".
        radiobutton_robot = browser.find_element_by_id("robotsRule")
        radiobutton_robot.click()
        # Нажать на кнопку Submit.
        submit = browser.find_element_by_css_selector("button.btn")
        submit.click()

        time.sleep(10)
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
    test("http://suninjuly.github.io/math.html", 'Lesson 1 Step 5')


if __name__ == '__main__':
    main()
