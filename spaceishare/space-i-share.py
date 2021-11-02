from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pandas as pd
import time

PATH="/home/aravind/Featurepreneur/chromedriver"

driver=webdriver.Chrome(PATH)

driver.get("https://spaceishare.com/")


search=driver.find_element_by_id('search')


search.send_keys('Calgary, AB, Canada')

search.send_keys(Keys.RETURN)

click=driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/div/div/div/div/span[2]/span/button").click()

links_space=[]

# for i in range(1,7):
i=0

while True:

    try:
        driver.find_element_by_xpath(f'/html/body/div[2]/div/div/div/div/div[1]/div[4]/div[4]/a[{i}]').click()

        page_links=driver.find_elements_by_xpath("//a[@class='font-weight-bolder']")

        for link in page_links:

            each_link=link.get_attribute('href')

            links_space.append(each_link)
        
        time.sleep(3)

        i+=1

    except:

        break
        
    
        

csv_list={

        'Links':links_space
    }

df=pd.DataFrame(csv_list)

df.to_csv('spacelinks.csv',mode='a+')



driver.quit()



