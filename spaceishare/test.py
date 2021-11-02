from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import pandas as pd
import time

PATH="/home/aravind/Featurepreneur/chromedriver"

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

driver.get("https://spaceishare.com/profile/myProfile/1051")

#  scroll = driver.find_elements_by_css_selector('#load_data_message > h3')
wait = WebDriverWait(driver, 10) 
prize=[]
parking=[]
while True: 
    
        prize_amount=1
        while True:
            try:
                amount=driver.find_element_by_css_selector(f'#product-id > div:nth-child({prize_amount}) > div > div > div.profile-prize').text
                prize.append(amount)
                prize_amount+=1
            except NoSuchElementException:
                break
        add_val=1
        while True:
            try:
                add=driver.find_element_by_xpath(f'//*[@id="product-id"]/div[{add_val}]/div/div/div[2]/a[1]/h5').text
                parking.append(add)
                add_val+=1
            except NoSuchElementException:
                break
        # profile_prize=driver.find_element_by_css_selector("#product-id > div:nth-child(1) > div > div > div.profile-prize").text
           
        
        try:

            wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="load_data_message"]/h3')))
            break
            
        except:    
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(3)
                
            

print(prize)
print(parking)  
print("done")