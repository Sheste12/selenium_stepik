from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as WDW
from selenium.webdriver. support import expected_conditions as EC
import tkinter
from tkinter import messagebox
import time
import traceback
import math

def test(link, n):
    try:
        # Открыть страницу http://suninjuly.github.io/explicit_wait2.html
        browser = webdriver.Chrome()
        browser.get(link)

        # Дождаться, когда цена дома уменьшится до $100 (ожидание нужно установить не меньше 12 секунд)
        btn = browser.find_element_by_id("book")
        WDW(browser, 12).until(
            EC.text_to_be_present_in_element((By.ID, "price"), "$100")
        )

        # Нажать на кнопку "Book"
        btn.click()

        # Решить уже известную нам математическую задачу (используйте ранее написанный код) и отправить решение
        x = browser.find_element_by_id("input_value").text
        y = calc(x)

        answer = browser.find_element_by_id("answer")
        answer.send_keys(y)

        submit = browser.find_element_by_id("solve")
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
    test("http://suninjuly.github.io/explicit_wait2.html", 'Lesson 4 Step 8')


if __name__ == '__main__':
    main()