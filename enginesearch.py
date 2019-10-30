import requests
from bs4 import BeautifulSoup

google_url = "https://www.google.com.tw/search"
w = input("搜尋(ex:動畫): ")
if len(w)==0: w = "動畫"
my_params = {'q': w}
print (w)
r = requests.get(google_url, params = my_params)
#print (r.status_code)

if r.status_code == requests.codes.ok:
  soup = BeautifulSoup(r.text, 'lxml')
  
  items = soup.find_all("div", class_="ZINbbc")
  #print(items)
for i in items:
    x = str(i.find_all("a")).split("=")
    if len(x)<8:    continue
    if len(x[6].split(">"))==1:    continue      
    #print(x , len(x[6].split(">")))
    #if x[6].find("/search?ie")==0:    continue 
    print  ()
    print  (x[6].split(">")[1].split("<")[0])
    if len(x[6].split(">")[1].split("<")[0]) == 0 : exit()
    print  (x[2].split("&")[0])
    
    #exit()