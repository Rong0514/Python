import os
import time
import sqlite3
import requests
import threading

def page1(): # 下載link小圖
    conn   = sqlite3.connect('lativ.db')
    cursor = conn.cursor()
    sql    = "select ID , serial_number , classification ,  path from stock order by ID asc"
    cursor.execute(sql)
    conn.commit()
    data   = cursor.fetchall()
    conn.close()
    for row in data:
        title  = row[1]
        classs = row[2]
        photo  = row[3]
        if not os.path.exists('static'):                                                  
            os.makedirs('static')
        subdir = os.path.join('static' , classs)
        if not os.path.exists(subdir):
            os.makedirs(subdir)
        try:                                                                           
            w = requests.get(photo)                                                     
        except requests.exceptions.RequestException as e:                               
            print(f"無法下載圖片 {photo}: {e}")                                           
            continue
        with open (os.path.join(subdir, title)+'.jpg', 'wb') as fObj:                                
            fObj.write(w.content)                                                                                                                       
            time.sleep(1)
    print('page_1 抓取完畢')

def page2(): # 下載內容大圖
    conn   = sqlite3.connect('lativ.db')
    cursor = conn.cursor()
    sql    = "select ID , serial_number , classification ,  link_url from stock order by ID asc"
    cursor.execute(sql)
    conn.commit()
    data   = cursor.fetchall()
    conn.close()
    for row in data:
        title  = row[1]
        title  = title + '-1'
        classs = row[2]
        photo  = row[3]      
        if not os.path.exists('static'):                                                  
            os.makedirs('static')
        subdir = os.path.join('static' , classs)
        if not os.path.exists(subdir):
            os.makedirs(subdir)
        try:                                                                           
            w = requests.get(photo)                                                     
        except requests.exceptions.RequestException as e:                               
            print(f"無法下載圖片 {photo}: {e}") 
        with open (os.path.join(subdir, title)+'.jpg', 'wb') as fObj:                                
            fObj.write(w.content)                                                                                                                       
            time.sleep(1)
    print('page_2 抓取完畢')

'''________________________________________________________________threading'''
t1 = threading.Thread(target = page1)
t2 = threading.Thread(target = page2)
t1.start()
t2.start()
t1.join()
t2.join()
print("Done.") 