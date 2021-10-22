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
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import csv

PATH = "/home/chaaya/softwares/chromedriver"
driver = webdriver.Chrome(PATH)


def startpy():
    driver.get("https://kalkinemedia.com/ca/companies")

    # prints title
    print(driver.title)

    # prints html source code
    print(driver.page_source)

if __name__ == '__main__':
    startpy()