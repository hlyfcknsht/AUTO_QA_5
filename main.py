from selenium import webdriver
from selenium.webdriver.common.by import By
import time



with webdriver.Chrome() as browser:
    browser.get('http://parsinger.ru/selenium/7/7.html')
    result = 0
    for i in browser.find_elements(By.TAG_NAME, "option"):
        result += int(i.text)
    input_result = browser.find_element(By.ID, "input_result").send_keys(result)
    browser.find_element(By.CLASS_NAME, "btn").click()
    print(browser.find_element(By.ID, 'result').text)
    time.sleep(30)
