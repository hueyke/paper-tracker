#!/usr/bin/env python3
from __future__ import print_function
from selenium import webdriver
import auth
import os

def getName():
    return 'GJI'

def getArticleStatus():
    url = 'https://mc.manuscriptcentral.com/gji'
    options = webdriver.ChromeOptions()
    options.add_argument('--window-size=1920,1080')
    options.add_argument('--disable-extensions')
    options.add_argument("--proxy-server='direct://'")
    options.add_argument('--proxy-bypass-list=*')
    options.add_argument('--start-maximized')
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--no-sandbox')
    options.add_argument('--ignore-certificate-errors')
    driver = webdriver.Chrome(options=options)
    driver.get(url)
    driver.find_element_by_id('USERID').send_keys(auth.getGJIUsername())
    driver.find_element_by_id('PASSWORD').send_keys(auth.getGJIPassword())
    driver.find_element_by_id('logInButton').click()
    driver.find_element_by_class_name('fa-pencil').click()
    result = driver.find_elements_by_class_name('pagecontents')
    result = result[1].text
    driver.quit()
    return result
        

if __name__ == '__main__':
    print(getArticleStatus())
