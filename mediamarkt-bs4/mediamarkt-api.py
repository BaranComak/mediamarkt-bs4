from cgitb import html
from urllib import response
import requests
from bs4 import BeautifulSoup
import time

url = "https://www.mediamarkt.com.tr/tr/category/_laptop-504926.html"
html = requests.get(url).content


soup = BeautifulSoup(html,"html.parser")
list = soup.find("ul",{"class":"products-list"}).find_all("div",{"class":"product-wrapper"})
num = 0
count = 0

for div in list:
    title = div.find("div",{"class":"content"}).find("a").text.strip() 
    count+=1  
    num+=1
    money = div.find("div",{"class":"price-box"}).find("div").text.strip(",-")    
    ozellik = div.find("dl",{"class":"product-details"}).text.strip()
    print(f"Ürün Adı: {title} | Ürün Fiyatı: {money}\n | Ürün Özellikleri: {ozellik}\n ")




            