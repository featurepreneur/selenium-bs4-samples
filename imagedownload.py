import requests
from bs4 import BeautifulSoup
import os
import re
import pandas as pd
import csv
    


def scrape_url(url):


     r = requests.get(url)
     soup = BeautifulSoup(r.text,'html.parser')

     # print(soup)

     div = soup.find_all('div', class_ = "search-box-bg")

     # print(div)
     get_images(div)


def get_images(div_tag):
     try:
          os.mkdir(os.path.join(os.getcwd(),'images'))
     except:
          pass
     os.chdir(os.path.join(os.getcwd(),'images'))
     for div in div_tag:
          style = div['style']
          link = style.split(";")[0].split('url')[1]
          img_tag = link[1:-1]
          
          # .split('(')[1].split(')')[0]
          
          # print(img_tag)

          picture = img_tag.split('/')
          name = picture[len(picture)-1]
          if '.' not in name:
                    name = name + '.jpg'
          with open(name,'wb') as f:
               
               img = requests.get(img_tag)
               f.write(img.content)
               print('writing: ', name)
          # i = img_tag[0]
          # img =  i.split('url')
          # prt = img[1]
          # h = prt.split('(')
          # k = h[1]
          # l = k.split(')')
          # print(img_tag)


if __name__ == '__main__':
    scrape_url('https://spaceishare.com/Listings')


