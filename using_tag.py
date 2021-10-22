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
    driver.get("https://www.asc-csa.gc.ca/eng/astronauts/space-medicine/projects.asp")

    # gets first element from the given tag
    onelink = driver.find_element_by_tag_name("a")
    print(onelink.text)

    # getting all the links in the website
    links = driver.find_elements_by_tag_name("a")
    for link in links:
        print(link.text)

    driver.quit()
if __name__ == '__main__':
    startpy()