from selenium import webdriver
from selenium.webdriver.support.ui import Select
import os
import tkinter
from tkinter import messagebox
import time
import traceback
import math

def test(link, n):
    try:
        # Открыть страницу http://suninjuly.github.io/file_input.html
        browser = webdriver.Chrome()
        browser.get(link)

        # Заполнить текстовые поля: имя, фамилия, email
        first_name = browser.find_element_by_name("firstname")
        first_name.send_keys("Eugeny")
        last_name = browser.find_element_by_name("lastname")
        last_name.send_keys("Listov")
        email = browser.find_element_by_name("email")
        email.send_keys("zhenya.listov@yandex.ru")

        # Загрузить файл. Файл должен иметь расширение .txt и может быть пустым
        cur_dir = os.path.abspath(os.path.dirname(__file__))
        file_path = os.path.join(cur_dir, "lesson2_step8.txt")
        sel_file = browser.find_element_by_id("file")
        sel_file.send_keys(file_path)

        # Нажать кнопку "Submit"
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
    test("http://suninjuly.github.io/file_input.html", 'Lesson 2 Step 8')


if __name__ == '__main__':
    main()
