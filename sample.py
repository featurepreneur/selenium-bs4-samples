#!/usr/bin/env python
# -*- coding: utf-8 -*-
# the above line is to avoid 'SyntaxError: Non-UTF-8 code starting with' error

'''
Created on 

Course work: 

@author:

Source:
    
'''

# Import necessary modules
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time 

PATH = "/home/chaaya/softwares/chromedriver"
driver = webdriver.Chrome(PATH)


def startpy():
    driver.get("https://spaceishare.com/Listings")
    element = driver.find_elements_by_class_name("search-box-bg")
    for ele in element:
        link = ele.get_attribute('style')
        print(link)
if __name__ == '__main__':
    startpy()