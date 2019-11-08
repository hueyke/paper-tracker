#!/usr/bin/env python3
from __future__ import print_function
from selenium import webdriver
import auth

def getName():
    return 'GJI'

def getArticleStatus():
    url = 'https://mc.manuscriptcentral.com/gji'
    driver = webdriver.Chrome('./chromedriver')
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
