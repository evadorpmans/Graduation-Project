import requests
from bs4 import BeautifulSoup
#import csv
import pandas as pd
import numpy as np
import random

links = []


url='https://www.ah.nl/producten/ontbijtgranen-en-beleg?page={page}'
for page in range(1,15):
    req = requests.get(url.format(page=page))
    soup = BeautifulSoup(req.content, 'html.parser')

    dfGP = pd.DataFrame(columns = ['product_name', 'allergies', 'p_price','verifications', 'rating', 'n_rating'])

    for link in soup.select('div[class="product-card-portrait_content__2xN-b"] a'):
        abs_url = 'https://www.ah.nl' + link.get('href')
        #print(abs_url)
       
        info_list = [None, None, None]
        
        #GETTING THE PRODUCT NAME
        product_name = []
        req2 = requests.get(abs_url)
        soup = BeautifulSoup(req2.content, 'html.parser')
        product_name = (soup.find(class_='line-clamp_root__1FX_J line-clamp_active__Yb_HA').text)
        #print(product_name)
        #product_name.append(product_name)
        
        #GETTING THE ALLERGY INFORMATION
        allergies = []
        req3 = requests.get(abs_url)
        soup2 = BeautifulSoup(req3.content, 'html.parser')
        allergies = [d.get_text() for d in soup2.select('dd[class="product-info-definition-list_value__kspp6"]')][2:-2]
        #print(allergies)
        #allergies.append(allergies)
        
        #GETTING THE PRICE
        p_price = []
        req4 = requests.get(abs_url)
        soup = BeautifulSoup(req4.content, 'html.parser')
        p_price = (soup.find(class_='price-amount_root__37xv2 product-card-hero-price_now__PlF9u'))
        p_price = p_price.text if p_price else None
        #print(p_price)
        #p_price.append(p_price)
        
        info_list[0] = product_name
        info_list[1] = allergies
        info_list[2] = p_price
        dfGP = dfGP.append({'product_name':info_list[0], 'allergies':info_list[1], 'p_price':info_list[2], 'verifications':random.randrange(0,2200), 'rating':np.random.uniform(0,5), 'n_rating':random.randrange(0,1000)}, ignore_index=True)
        dfGP.to_csv(r'/Users/evadorpmans/Desktop/MDDD/GRADUATION/DataGP.csv')
        #print(df)









