import time
from selenium import webdriver
from selenium.webdriver.common.by import By

import os, pickle

#from pages.base import WebPage
#from pages.elements import WebElement
#from pages.elements import ManyWebElements
import test_selenium_auth
import json

def test_add_role():
    driver = webdriver.Chrome('C:\selenium\chromedriver_win32/chromedriver.exe')
    driver.get('https://dev.lectonic.ru')
    # Opening JSON file
    f = open('cookies.txt')
    # returns JSON object as
    data = json.load(f)
    print(data)
    driver.add_cookie(data)
    time.sleep(5)
    # Open Lectonic add role page:
    driver.get('https://dev.lectonic.ru/add_role')

    time.sleep(1)
    #
    # # add role
    role = driver.find_element_by_xpath("//button[contains(text(), 'Лектор')]")
    role.click()
    time.sleep(1)
    #

    # # topic
    add_topic = driver.find_element_by_class_name('dropdown__input')
    add_topic.click()
    time.sleep(2)
    topics = driver.find_elements_by_class_name('dropdown-item')
    for topic in topics:
        if topic.text == 'Информационные технологии':
            topic.click()
            break
    time.sleep(2)

    #
    # # add link publication
    add_link_pub = driver.find_elements_by_class_name('input__add-link')[1]
    add_link_pub.click()
    add_link_pub.send_keys('https://lectonic.ru/')
    time.sleep(1)
    driver.find_elements_by_xpath('//img[@alt="добавить ссылку"]')[1].click()
    time.sleep(1)
    #
    # # btn next step
    btn_next_step = driver.find_element_by_xpath("//button[contains(text(), 'Следующий шаг')]")
    btn_next_step.click()
    time.sleep(1)
    #
    # # education
    education = driver.find_element_by_class_name('form__textarea')
    education.click()
    education.send_keys('Московский Государственный Институт Электроники и Математики')
    time.sleep(1)

    # # btn next step2
    btn_next_step2 = driver.find_element_by_xpath("//button[contains(text(), 'Следующий шаг')]")
    btn_next_step2.click()
    time.sleep(1)

    # # lecture room
    # # equipment

    # # btn checkbox
    checkbox = driver.find_element_by_id("checkbox")
    checkbox.click()
    time.sleep(2)

    # # btn complete registration
    btn_complete_reg = driver.find_element_by_xpath("//button[contains(text(), 'Завершить регистрацию')]")
    btn_complete_reg.click()
    time.sleep(2)



    # Make the screenshot of driver window:
    driver.save_screenshot('add_role.png')






