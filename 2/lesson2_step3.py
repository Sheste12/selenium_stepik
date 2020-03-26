from selenium import webdriver
from selenium.webdriver.support.ui import Select
import tkinter
from tkinter import messagebox
import time
import traceback
import math

def test(link, n):
    try:
        # Открыть страницу http://suninjuly.github.io/selects1.html.
        browser = webdriver.Chrome()
        browser.get(link)

        # Посчитать сумму заданных чисел
        num1 = browser.find_element_by_id("num1").text
        num2 = browser.find_element_by_id("num2").text
        summation = str( int(num1) + int(num2) )
        # Выбрать в выпадающем списке значение равное расчитанной сумме
        sel = Select(browser.find_element_by_tag_name("select"))
        sel.select_by_value(summation)
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
    test("http://suninjuly.github.io/selects1.html", 'Lesson 2 Step 3 Test 1')
    test("http://suninjuly.github.io/selects2.html", 'Lesson 2 Step 3 Test 2')


if __name__ == '__main__':
    main()
