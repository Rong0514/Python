import sqlite3
import requests
from bs4 import BeautifulSoup

conn   = sqlite3.connect('lativ.db')
cursor = conn.cursor()
sql    = "select * from stock order by ID asc"
cursor.execute(sql)
conn.commit()
data   = cursor.fetchall()
conn.close()

for row in data:
    ID             = row[0]
    link_url       = row[5]

    session = requests.session()                        
    url1    = link_url                                 
    header  = {'User-Agent':
          'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36'
          }
    data    = session.get(url1 , headers = header)      
    soup    = BeautifulSoup(data.text , 'html.parser')   
    page2   = soup.select_one('div.product_image img').get('src')
    conn    = sqlite3.connect('lativ.db')
    cursor  = conn.cursor()
    sql     = "update stock set link_url = ? where id = ?"
    cursor.execute(sql , (page2, ID))
    conn.commit()
conn.close()