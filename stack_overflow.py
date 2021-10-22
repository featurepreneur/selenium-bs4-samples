import requests
from bs4 import BeautifulSoup
import re
import pandas as pd
import csv
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


PATH = "/home/chaaya/softwares/chromedriver"
driver = webdriver.Chrome(PATH)


def scrape(url):

    r = requests.get(url)
    soup = BeautifulSoup(r.text,'html.parser')

    user(soup) 

def user(soup):
    names = soup.find_all('div', class_ = "user-details")
    for name in names:
        print(name.a.text)

get_url():


def startpy():
    driver.get(url)
        # soup = scrape(f'https://stackoverflow.com/users?page=2&tab=reputation&filter=week')
    scrape(url)
    elm = driver.find_element_by_xpath('//*[@id="user-browser"]/div[2]/a[6]')

        elm.click()

    # user(soup)
    # print(f'Getting page:{i}')
        


if __name__ == "__main__":
    startpy()
    

