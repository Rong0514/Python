from selenium import webdriver               
from selenium.webdriver.common.by import By  
from bs4 import BeautifulSoup                
import urllib.parse                          
import time                                  
import re                                    
import pandas as pd                          


global pages
pages = int(input("輸入頁數(1頁 = 15筆) : "))

driver = webdriver.Chrome()                                                  
driver.implicitly_wait(10)     

urls = ['https://ifoodie.tw/explore/list?sortby=rating',
        'https://ifoodie.tw/explore/list?sortby=recent',
        'https://ifoodie.tw/explore/list?sortby=popular']

addresses = set() 

for url in urls:
    driver.get(url)
    food = []
    
    for i in range(pages):                                                          
        element = driver.find_element(By.CSS_SELECTOR,'div.jsx-987803290.scroll-box') 
        driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", element) 
        time.sleep(8)  
                                                           
        data    = driver.page_source
        soup    = BeautifulSoup(data , 'html.parser')
        total   = soup.select_one('div.jsx-987803290.item-list')
        title   = total.select('div.jsx-1309326380.title a')
        photo   = total.select('div.jsx-1309326380.restaurant-info img')
        addre   = total.select('div.jsx-1309326380.address-row')
        price   = total.select('div.jsx-1309326380.avg-price')
        star    = total.select('div.jsx-2373119553.text')
        feature = total.select('div.jsx-1309326380.category-row')
        for row1,row2,row3,row4,row5,row6 in zip(title,photo,addre,price,star,feature):
            title         = row1.text
            if row2.get('src') == 'data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==':
                photo_url = row2.get('data-src')
            else:
                photo_url = row2.get('src')
            address       = row3.text
            price_text    = row4.text
            price         = re.findall('\d+', price_text)
            link_url      = 'https://ifoodie.tw/'+urllib.parse.unquote(row1.get('href'))
            if price:
                price     = price[0]
            else:
                price     = '沒有找到均消'
            star          = row5.text
            feature       = row6.text[4:]

            if address in addresses: continue
            addresses.add(address) 
                    
            food.append({"title"    : title,
                         "link_url" : link_url,
                         "photo_url": photo_url,
                         "address"  : address,
                         "price"    : price,
                         "star"     : star,
                         "feature"  : feature})
            
        driver.find_element(By.CSS_SELECTOR,"li.next a").click() 
df = pd.DataFrame(food)                                          
df.to_csv('output.csv' , index = False , encoding = 'utf-8-sig')
driver.quit()                                                    