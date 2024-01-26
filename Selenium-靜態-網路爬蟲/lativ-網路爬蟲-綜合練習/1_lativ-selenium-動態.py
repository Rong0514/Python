import os
import time
import random
import sqlite3
from bs4 import BeautifulSoup
from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

db_name        = 'lativ.db'
db_exists      = os.path.exists(db_name)
conn = sqlite3.connect('lativ.db')
if db_exists  == True:
    print("Database file exists, opened successfully.")
else:
    sql = "create table 'stock' ('ID' INTEGER PRIMARY KEY AUTOINCREMENT, 'serial_number' TEXT, 'classification' TEXT, 'title' TEXT, 'price' TEXT, 'link_url' TEXT, 'path' TEXT);"
    conn.execute(sql)
    conn.commit()
conn.close()

driver = webdriver.Chrome()                                           
driver.implicitly_wait(3)                                              
driver.get("https://www.lativ.com.tw/")

element      = driver.find_element(By.TAG_NAME, 'body')
actions      = ActionChains(driver)
actions.move_to_element_with_offset(element, 5, 5).click().perform()

link_url = ['a[href="https://www.lativ.com.tw/WOMEN"]',
            'a[href="https://www.lativ.com.tw/MEN"]',
            'a[href="https://www.lativ.com.tw/KIDS"]']

class_sort   = ['女裝','男裝','童裝']

for link, classs in zip(link_url, class_sort):
    element      = driver.find_element(By.CSS_SELECTOR , link).click()
    
    start_height = driver.execute_script("return document.body.scrollHeight")
    while True:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)
        end_height    = driver.execute_script("return document.body.scrollHeight")
        if end_height == start_height:
            break
        start_height  = end_height
    
    data  = driver.page_source
    soup  = BeautifulSoup(data , 'html.parser')
    photos      = soup.select('ul.list_display.list_outfit li a img')
    links       = soup.select('ul.list_display.list_outfit li a')
    title       = soup.select('div.productname')
    price_total = soup.select('span.hidden')
    for row1, row2, row3, row4 in zip(photos , title , price_total , links):
        link  = row4.get('href')
        link  = 'https://www.lativ.com.tw'+link
        photo = row1.get('src')
        # print('title : ' , row2.text)
        # print('link  : ' , link)
        # print('photo : ' , photo)
        # if row3.select('span.activities'):
        #     price = row3.select('span.currency.symbol')
        #     price = price[1]
        #     print('price : ', price.text.strip())
        # else:
        #     price = row3.select_one('span.currency.symbol')
        #     print('price : ', price.text)
        # print('-'*60)
        
        '''__________________________________________________________sql'''
        conn    = sqlite3.connect('lativ.db')
        cursor  = conn.cursor()
        
        def generate_serial_number(classs):
            prefix = {'男裝': 'M', '女裝': 'W', '童裝': 'K'}[classs]
            while True:
                serial_number = prefix + str(random.randint(10000, 99999))
                cursor.execute("select * from stock where serial_number = ?", (serial_number,))
                if cursor.fetchone() is None:
                    return serial_number
        serial_number = generate_serial_number(classs)
        classification = classs
        T = row2.text
        if row3.select('span.activities'):
            price = row3.select('span.currency.symbol')
            price = price[1]
            price = price.text.strip()
        else:
            price = row3.select_one('span.currency.symbol')
            price = price.text   
        P = photo
        L = link
        
        conn    = sqlite3.connect('lativ.db')
        cursor  = conn.cursor()
        sql     = "insert into stock (serial_number , classification , title , price , link_url , path) values(? , ? , ? , ?, ? , ?)"
        cursor.execute(sql , (serial_number , classification , T , price , L , P))
        conn.commit()   
conn.close()
driver.quit()