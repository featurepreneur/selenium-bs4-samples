from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pandas as pd
import time

PATH="/home/chaaya/softwares/chromedriver"

driver=webdriver.Chrome(PATH)

driver.get("https://www.spaceishare.com/")
driver.maximize_window()

driver.find_element_by_css_selector("#header > div > nav > ul > li:nth-child(6) > a").click()
# driver.find_element_by_css_selector("#login_form > div.row > div.col-md-7 > a").click()
email = driver.find_element_by_name("email")
email.send_keys("iambored2985@gmail.com")
pwd = driver.find_element_by_name("pwd")
pwd.send_keys('tactlabs123')
driver.find_element_by_name("login").click()

driver.get("https://spaceishare.com/profile/myProfile/1")

#  scroll = driver.find_elements_by_css_selector('#load_data_message > h3')


while True: 
    try:
        scroll = driver.find_elements_by_css_selector('#load_data_message > h3')
        print(scroll.text)
        break
    except:    
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(3)
        


print("done")