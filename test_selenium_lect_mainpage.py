import time
from selenium import webdriver


def test_main_page():
    driver = webdriver.Chrome('C:\selenium\chromedriver_win32/chromedriver.exe')

    # Open Lectonic main page:
    driver.get('http://dev.lectonic.ru')

    time.sleep(2)  # just for demo purposes, do NOT repeat it on real projects!

    # Find the field for auth:
    btn_newuser = driver.find_element_by_xpath("//button[contains(text(), 'Присоединиться')]")
    btn_newuser.click()

    time.sleep(2)  # just for demo purposes, do NOT repeat it on real projects!

    # add email
    input_email = driver.find_element_by_class_name('signUpEmail')
    input_email.click()

    input_email.send_keys('test-1_test.1@mail.ru')
    # Make the screenshot of driver window:
    driver.save_screenshot('input_email.png')
    time.sleep(2)

    # label auth__form__checkbox-signUpLabel
    label_signUp = driver.find_element_by_id("auth__form__checkbox-signUpLabel")
    label_signUp.click()

    time.sleep(2)

    # btn registration
    btn_registration = driver.find_element_by_xpath("//button[contains(text(), 'Зарегистрироваться')]")
    btn_registration.click()

    time.sleep(2)

    # Make the screenshot of driver window:
    driver.save_screenshot('result.png')