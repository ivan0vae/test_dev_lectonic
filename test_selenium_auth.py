import time
from selenium import webdriver
import json

def test_auth():
    driver = webdriver.Chrome('C:\selenium\chromedriver_win32/chromedriver.exe')

    # Open Lectonic main page:
    driver.get('http://dev.lectonic.ru')

    time.sleep(2)  # just for demo purposes, do NOT repeat it on real projects!

    # Find the field for auth:
    btn_user = driver.find_element_by_xpath("//button[contains(text(), 'Присоединиться')]")
    btn_user.click()

    time.sleep(2)  # just for demo purposes, do NOT repeat it on real projects!

    # Find the field for auth:
    btn_entry = driver.find_element_by_class_name('auth__link')
    btn_entry.click()

    # input email
    input_email = driver.find_element_by_name('email')
    input_email.click()
    input_email.clear()
    input_email.send_keys('test-1_test.1@mail.ru')

    # input pass
    input_password = driver.find_element_by_name('password')
    input_password.click()
    input_password.clear()
    input_password.send_keys('12345678')

    time.sleep(2)

    # btn ComeIn
    btn_ComeIn = driver.find_element_by_xpath("//button[contains(text(), 'Войти')]")
    btn_ComeIn.click()

    time.sleep(2)
    c = driver.get_cookie('auth_token')
    with open('cookies.txt', 'w') as f:
        json.dump(c, f)

    # Make the screenshot of driver window:
    driver.save_screenshot('result_auth.png')