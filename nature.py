import requests
from bs4 import BeautifulSoup
url = "https://www.nature.com/research-analysis"
r = requests.get(url)
soup = BeautifulSoup( r.text , "lxml")
x = soup.find_all("div" , class_="c-article-item__content c-article-item--with-image")
for i in x:
    print (i.text.split("\n")[7])
    print("https://www.nature.com" + str(i).split("href=")[1].split(">\n<")[0].split('"')[1])
    print()