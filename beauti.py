from bs4 import BeautifulSoup
import requests

webpage = requests.get('https://www.banggood.in/search/game-console.html?from=nav')
sp = BeautifulSoup(webpage.content,'html.parser')
#print(sp.text)
title = sp.find_all('a','title')
sellprice = sp.find_all('span','price')
orignprice = sp.find_all('span','price-old')
review = sp.find_all('a','review')

titleloop = [titles.text for titles in title]
#sellpriceloop = [sell.text for sell in sellprice]
orignpriceloop = [orign.text for orign in orignprice]
reviewloop = [reviews.text for reviews in review]

#print(sellpriceloop)
data = {'Name_of_console':titleloop,
        
        'Number_of_review':reviewloop}

import pandas as pd
df = pd.DataFrame(data,columns=['Name_of_console','Number_of_review'])
df.to_excel('C:/Programes/python programes/beauti.py.xlsx',index = False)
'''
print(len(sellpriceloop))
print(len(titleloop))
print(len(orignpriceloop))
print(len(reviewloop))
'''