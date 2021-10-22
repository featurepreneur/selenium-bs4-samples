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
    driver.get("https://www.google.com/")

    # gets first element from the given tag
    search = driver.find_element_by_name("q")
    search.send_keys("cats")
    search.send_keys(Keys.RETURN)
    
    time.sleep(5)

    driver.quit()
if __name__ == '__main__':
    startpy()