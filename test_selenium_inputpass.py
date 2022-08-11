import time
from selenium import webdriver


def test_input_password():
    driver = webdriver.Chrome('C:\selenium\chromedriver_win32/chromedriver.exe')

    # Open link from email:
    driver.get('https://dev.lectonic.ru/confirm_email?key=9e2e850ae7861b') #input link from email

    time.sleep(2)  # just for demo purposes, do NOT repeat it on real projects!

    # add password
    input_password = driver.find_element_by_name('password')
    input_password.click()
    input_password.send_keys('12345678')

    #repeat password
    input_password2 = driver.find_element_by_name('password2')
    input_password2.click()
    input_password2.send_keys('12345678')

    time.sleep(2)

    # btn signup
    btn_signup = driver.find_element_by_xpath("//button[contains(text(), 'Продолжить')]")
    btn_signup.click()

    time.sleep(2)

    # Make the screenshot of driver window:
    driver.save_screenshot('result_signup.png')