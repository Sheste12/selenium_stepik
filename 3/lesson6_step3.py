import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as WDW
from selenium.webdriver.support import expected_conditions as EC
import time
import math

@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()

@pytest.mark.parametrize(
    "link",
    [
        "236895",
        "236896",
        "236897",
        "236898",
        "236899",
        "236903",
        "236904",
        "236905"
    ]
)
def test_stepik(browser, link):
    browser.get(f"https://stepik.org/lesson/{link}/step/1")
    textarea_answer = WDW(browser, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".string-quiz__textarea"))
    )
    answer = str( math.log(int(time.time())) )
    textarea_answer.send_keys(answer)
    submit = WDW(browser, 3).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, ".submit-submission"))
    )
    submit.click()
    answer = WDW(browser, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".smart-hints__hint"))
    )
    assert answer.text == "Correct!"
