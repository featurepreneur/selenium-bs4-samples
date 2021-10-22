import requests
from bs4 import BeautifulSoup
import pandas as pd
import csv 
#url = "https://www.linkedin.com/in/aishwarya-kapoor-6019a51a2/"

linkedin=[]
def get_soup(url):
    response=requests.get(url)
    soup= BeautifulSoup(response.text,'html.parser')
    return soup

def get_reviews(soup): 
    profiles = soup.find('div',{'class':'pv-text-details__left-panel mr5'})
    try:
        print("inside try")
        #for item in profiles:
        details = {
        'name':profiles.find('h1', {'class':'text-heading-xlarge inline t-24 v-align-middle break-words'}).text,
        'location ':profiles.find('span',{'class':'text-body-small inline t-black--light break-words'}).text
        # 'about':item.find('i',{'data-hook':'review-star-rating'}).text,
        # 'experience': item.find('span',{'data-hook':'review-body'}).text.strip(),
        # 'education': item.find('span',{'data-hook':'review-body'}).text.strip(),
        # 'Licenses&certificates': item.find('span',{'data-hook':'review-body'}).text.strip(),
        # 'volunter-experience': item.find('span',{'data-hook':'review-body'}).text.strip(),
        # 'skills': item.find('span',{'data-hook':'review-body'}).text.strip(),
        # 'Accomplishments': item.find('span',{'data-hook':'review-body'}).text.strip()
        }
        linkedin.append(details)
        for link in linkedin:
            print(link)
    except:
        pass


def startpy():
    soup = get_soup('https://www.linkedin.com/in/aishwarya-kapoor-6019a51a2/')
    get_reviews(soup)


    # df = pd.DataFrame(linkedin)
    # df.to_csv('profile.csv')
    print('End')

if __name__ == '__main__':
    startpy()