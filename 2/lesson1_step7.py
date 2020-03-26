from selenium import webdriver
import tkinter
from tkinter import messagebox
import time
import traceback
import math

def test(link, n):
    try:
        # Открыть страницу http://suninjuly.github.io/get_attribute.html.
        browser = webdriver.Chrome()
        browser.get(link)
        # Найти на ней элемент-картинку, который является изображением сундука с сокровищами.
        img = browser.find_element_by_id("treasure")
        # Взять у этого элемента значение атрибута valuex, которое является значением x для задачи.
        x = img.get_attribute("valuex")
        # Посчитать математическую функцию от x (сама функция остаётся неизменной).
        y = calc(x)
        # Ввести ответ в текстовое поле.
        answer = browser.find_element_by_id("answer")
        answer.send_keys(y)
        # Отметить checkbox "I'm the robot".
        checkbox_robot = browser.find_element_by_id("robotCheckbox")
        checkbox_robot.click()
        # Выбрать radiobutton "Robots rule!".
        radiobutton_robot = browser.find_element_by_id("robotsRule")
        radiobutton_robot.click()
        # Нажать на кнопку "Submit".
        submit = browser.find_element_by_css_selector("button.btn")
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
    test("http://suninjuly.github.io/get_attribute.html", 'Lesson 1 Step 7')


if __name__ == '__main__':
    main()
