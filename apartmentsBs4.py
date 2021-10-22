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
import requests
from bs4 import BeautifulSoup
import pandas as pd
import csv

apartments=[]
csv_file = open('apartment.csv', 'w')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['column1'])

def get_soup(url):
    response=requests.get(url)
    soup= BeautifulSoup(response.text,'html.parser')
    return soup

def get_apt(soup):
    toronto_apt = soup.find_all('a',class_ = 'result-title hdrlnk')
    try:
        for apt in toronto_apt:
            apartments.append(apt.text)   
    except:
        pass

def startpy():
    for i in range(11):
        soup = get_soup(f'https://toronto.craigslist.org/d/apartments-housing-for-rent/search/apa?s={i*120}&query=parking%20space&sort=rel')
        print(f'Getting page:{i}')
        get_apt(soup)
        # print(len(apartments))
        if soup.find('a',class_ = 'result-title hdrlnk'):
            pass
        else:
            break
            # csv_writer.writerow([apartments])
        
    df = pd.DataFrame(apartments)
    df.to_csv('apartment.csv')
    print('End')

csv_file.close
        
if __name__ == '__main__':
    startpy()