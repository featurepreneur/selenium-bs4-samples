import requests
from bs4 import BeautifulSoup
import re
import pandas as pd
import csv


def scrape(url):

    r = requests.get(url)
    soup = BeautifulSoup(r.text,'html.parser')

    # print(soup)

    # dict1 = badges(soup)
    dict2 = stats(soup)

    # csv_file(dict1,dict2)


# def badges(soup):

#     number = []
#     badges = []

#     div_tag = soup.find_all('div', class_ = "d-flex gs16 gsx d-flex ai-center")

#     for div in div_tag:

#         no_div = div.find('div', class_ = "fs-title fw-bold fc-black-800").text
#         no = no_div.strip()
#         div_badges = div.find('div', class_ = "fs-caption").text
#         badge = div_badges.strip() 
#         number.append(no)
#         badges.append(badge)
#     badge_dict = {badges[i]: [number[i]] for i in range(len(badges))}

#     return badge_dict
    # print(badge_dict)

def stats(soup):
    list1 = []
    list2 = []
    numbers = []

    div_tag = soup.find('div',class_ = "d-flex flex__allcells6 gs16 fw-wrap md:jc-space-between")

    all_div = div_tag.find_all('div',class_ = "flex--item md:fl-auto")
    for div in all_div:
        num = div.find('div',class_ = "fs-body3 fc-dark").text
        numbers.append(num)
        d = div.text.strip()
        list1.append(d)

    print(list1)
    for i in list1:
        # print(i)
        a = i.replace(' ','')
        list2.append(a)
    list2 = [i.split('\n')[1] for i in list2]
    # print(list2)

    
    stat_dict = {list2[i]: [numbers[i]] for i in range(len(numbers))}
    print(stat_dict)
    # return stat_dict

# def csv_file(dict1,dict2):
#     dict2.update(dict1)
#     print(dict2)
    
#     df = pd.DataFrame.from_dict(dict2) 
#     df.to_csv (r'test8.csv', index = False, header=True)



if __name__ == "__main__":
    scrape("https://stackoverflow.com/users/10597533/sergei-mikhailovskii")