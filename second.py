import requests
from bs4 import BeautifulSoup
r=requests.get('https://www.edureka.co')
c=r.content
soup=BeautifulSoup(c,'html.parser')
for link in soup.find_all('a'):
    print(link.get('href'))
