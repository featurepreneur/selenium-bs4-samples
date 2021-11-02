from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

PATH="/home/aravind/Featurepreneur/chromedriver"

driver=webdriver.Chrome(PATH)

driver.get("https://spaceishare.com/listing/parking-space/ontario/toronto/secure-underground-parking-13030")

hosted_by=driver.find_element_by_xpath('//*[@id="contact_form"]/div/div/p/a').text
print(hosted_by)

type_of_space=driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div[1]/div[4]/div/p[4]').text
print(type_of_space)


space_fea_list=[]
space_fea=driver.find_elements_by_xpath("//p[@class='p-font-size']")


for text in space_fea:

    text_of_sf=text.text
    space_fea.append(text_of_sf)

listToStr = ' '.join(map(str, space_fea_list))
print(listToStr)
driver.quit()