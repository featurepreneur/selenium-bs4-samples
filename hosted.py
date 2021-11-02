from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.common.exceptions import NoSuchElementException
from  bs4 import BeautifulSoup
import requests

PATH="/home/aravind/Featurepreneur/chromedriver"

driver=webdriver.Chrome(PATH)

link1="https://spaceishare.com/listing/parking-space/ontario/toronto/parking-at-finch-and-younge-area-21184"
link=driver.get(link1)

# hosted_by=driver.find_element_by_xpath('//*[@id="contact_form"]/div/div/p/a').text
# print(hosted_by)

# type_of_space=driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div[1]/div[4]/div/p[4]').text
# print(type_of_space)

# sp_det=driver.find_elements_by_css_selector("body > div.upload_page.desktop-view.showlisting > div > div:nth-child(2) > div.col-md-6.float-left.position-relative.bg-white.pad-none.content-section > div.row.mr-30.row-pad > div > p:nth-child(6)").text
# print(sp_det)
# count=1
space_fea_list=[]

# while True:
#     try:
#         space_fea=driver.find_elements_by_xpath(f"//p[@class='p-font-size'][{count}]")


#         for text in space_fea:

#             text_of_sf=text.text
            
#             space_fea.append(text_of_sf)

#     except NoSuchElementException:
#         break
# print(spa)
# listToStr = ' '.join(map(str, space_fea_list))
# print(listToStr)

res=requests.get(link1)
html_page=res.content
soup=BeautifulSoup(html_page,'html.parser')
mydivs = soup.find("div", {"class": "row mr-30 row-pad"})
for t in mydivs.find_all("p", {"class": "p-font-size"}):
    a=t.text.strip()
    space_fea_list.append(a)

print(space_fea_list) 
driver.quit()