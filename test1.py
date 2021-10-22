import requests
from bs4 import BeautifulSoup


books_list=[]
      
url = f'http://www.gutenberg.org/browse/scores/top'
response = requests.get(url)
soup = BeautifulSoup(response.text,'html.parser')
books = soup.find('ol')
names = books.find_all('li')

# print(books)
        # books = soup.find_all("a", {"class": "absolute w-100 h-100 z-1"})

try:
    for name in names:
        books_list.append(name.text)   
        print (name.text)

except:
        pass