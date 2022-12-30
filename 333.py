import requests
from bs4 import BeautifulSoup
url = "https://www.mcdonalds.com/tw/zh-tw/full-menu.html"
Data = requests.get(url)
#print(Data.text)
sp = BeautifulSoup(Data.text, "html.parser")
result=sp.select(".cmp-category__item-name")
info = ""
for item in result:
	info += item.text + "\n\n"
print(info)