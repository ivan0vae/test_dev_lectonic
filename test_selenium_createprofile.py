import time
from selenium import webdriver
from selenium.webdriver.common.by import By

import os, pickle

#from pages.base import WebPage
#from pages.elements import WebElement
#from pages.elements import ManyWebElements
import test_selenium_auth
import json

def test_create_profile():
    driver = webdriver.Chrome('C:\selenium\chromedriver_win32/chromedriver.exe')
    driver.get('https://dev.lectonic.ru')
    # Opening JSON file
    f = open('cookies.txt')
    # returns JSON object as
    data = json.load(f)
    print(data)
    driver.add_cookie(data)
    time.sleep(1)
    # Open Lectonic create profile page:
    driver.get('https://dev.lectonic.ru/create_profile')

    time.sleep(1)

    # # add last_name
    input_last_name = driver.find_element_by_name('last_name')
    input_last_name.click()
    input_last_name.send_keys('Иванова')
    #
    # # add first_name
    input_first_name = driver.find_element_by_name('first_name')
    input_first_name.click()
    input_first_name.send_keys('Екатерина')

    time.sleep(1)
    # add middle_name
    #input_middle_name = driver.find_element_by_name('middle_name')
    #input_middle_name.click()
    #input_middle_name.send_keys('Александровна')

    time.sleep(1)

    #dropdown city
    dd_city = driver.find_element_by_class_name('dropdown__input')
    dd_city.click()
    dd_city.send_keys("Москв")
    time.sleep(1)
    dd_city.send_keys("а")
    time.sleep(1)
    driver.find_element_by_class_name('dropdown-item').click()
    time.sleep(1)

    #dropdown day
    dd_day = driver.find_element_by_name('day')
    dd_day.click()
    time.sleep(1)
    days = driver.find_elements_by_class_name('dropdown-item')
    for day in days:
        if day.text == '4':
            day.click()
            break
    time.sleep(1)

    #
    #dropdown month
    dd_month = driver.find_element_by_name('month')
    dd_month.click()
    time.sleep(1)
    months = driver.find_elements_by_class_name('dropdown-item')
    for month in months:
        if month.text == 'Августа':
            month.click()
            break
    time.sleep(1)
    #
    # #dropdown year
    dd_year = driver.find_element_by_name('year')
    dd_year.click()
    time.sleep(1)
    years = driver.find_elements_by_class_name('dropdown-item')
    for year in years:
        print(year.text)
        if year.text == '1990':
            year.click()
            break
    time.sleep(1)
    #
    # # add information
    input_info = driver.find_element_by_class_name('form__textarea')
    input_info.click()
    input_info.send_keys('Тестирование программных продуктов')
    time.sleep(5)
    #
    # # btn proceed
    btn_proceed = driver.find_element_by_class_name('userInfo__btn')
    btn_proceed.click()
    time.sleep(2)



