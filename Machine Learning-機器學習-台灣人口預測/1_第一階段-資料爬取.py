import re
import time
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import threading

def test1():
    '''____________________________________________建立webdriver物件 > 並啟動網址'''
    driver = webdriver.Chrome()                                                  
    driver.implicitly_wait(10)  
    driver.get('https://gis.ris.gov.tw/dashboard.html?key=B01')
    
    '''____________建立空DataFrame用於儲存資料 > 建立迴圈並帶上記載 年份 及 月份'''
    all_data = pd.DataFrame()
    for year in range(87 , 100):
        months = range(1 , 13)
        if year == 99: months = range(1 , 12) # 由於 99 年 縣市變動所以分兩個檔案抓取
        for month in months:
            
            '''__________________________________________________動態選取年份'''
            select_elements = driver.find_elements(By.CSS_SELECTOR , 'div.col-md-9 > select.input-sm.mb-md')
            Select_years    = Select(select_elements[0])
            Years           = Select_years.select_by_value(str(year))
    
            '''__________________________________________________動態選取月份'''
            select_elements = driver.find_elements(By.CSS_SELECTOR , 'div.col-md-9 > select.input-sm.mb-md')
            Select_month    = Select(select_elements[1])
            Month           = Select_month.select_by_value(str(month))
            print(year , "年" , " " , month , "月")
            
            '''______________________________________點擊搜尋按鈕 >並解析HTML'''
            driver.find_element(By.CSS_SELECTOR, 'button.pull-right.mb-xs.mt-xs.mr-xs.btn.btn-primary').click()
            time.sleep(3)
            data        = driver.page_source
            soup        = BeautifulSoup(data , 'html.parser')
    
            '''所有資料共5頁 > 點擊下一頁 並解析 > 將所有資訊疊帶進串列 > 並重複解析'''
            popula = []
            for i in range(5):
                population = soup.select('#datatable')
                for row in population:
                    tds = row.select('td')
                    for td in tds:
                        popula.append(td.text)
                    driver.find_element(By.CSS_SELECTOR, '#datatable_paginate > ul.pagination > li.next > a > span.fa.fa-chevron-right').click()
                    time.sleep(0.3)
                    data        = driver.page_source
                    soup        = BeautifulSoup(data , 'html.parser')
    
            '''_____________對popula串列進行字串處理 > 並設定pd所需要的三大資訊'''
            count       = len(popula)
            Citys       = []
            pop_numbers = []
            index       = str(year) + "年" + str(month) + '月'
            for i in range(count):
                if i % 2 == 0:
                    remove_city_number  = re.sub('\d', '', popula[i])
                    popula[i] = remove_city_number
                    Citys.append(remove_city_number)
                if i % 2 != 0:
                    remove_commas = popula[i].replace("," , "")
                    popula[i] = remove_commas
                    pop_numbers.append(remove_commas)
    
            '''將整理好的字串帶入 >  並帶入原始資料 + 新資料 > 並重複疊帶 > 最後 輸出檔案'''
            df = pd.DataFrame(columns=Citys, index=[index], data=[pop_numbers])
            all_data = pd.concat([all_data, df])
            print(all_data)
            
    file_name = "舊縣市人口統計表87年1月-99年11月.csv"
    all_data.to_csv(file_name)
    driver.quit()
    print('test1 done')
    
def test2():
    '''____________________________________________建立webdriver物件 > 並啟動網址'''
    driver = webdriver.Chrome()                                                  
    driver.implicitly_wait(10)  
    driver.get('https://gis.ris.gov.tw/dashboard.html?key=B01')
    
    '''________________建立空DataFrame用於儲存資料 > 建立迴圈並帶上記載 年份 及 月份'''
    all_data = pd.DataFrame()
    for year in range(99 , 114):
        if year == 99:
            months = range(12, 13)  # 只针对99年的12月
        else:
            months = range(1, 13)   # 其他年份的所有月份
            
        for month in months:
            '''__________________________________________________動態選取年份'''
            select_elements = driver.find_elements(By.CSS_SELECTOR , 'div.col-md-9 > select.input-sm.mb-md')
            Select_years    = Select(select_elements[0])
            Years           = Select_years.select_by_value(str(year))
            
            '''____________動態選取月份 > 如果月份不再則跳出迴圈(配合最新年月份)'''
            select_elements = driver.find_elements(By.CSS_SELECTOR , 'div.col-md-9 > select.input-sm.mb-md')
            Select_month    = Select(select_elements[1])
            options         = [option.get_attribute('value') for option in Select_month.options]
            if str(month) not in options : 
                file_name = "新縣市人口統計表99年12月.csv"
                all_data.to_csv(file_name)
                break
            Month           = Select_month.select_by_value(str(month))
            print(year , "年" , " " , month , "月")
            
            '''______________________________________點擊搜尋按鈕 >並解析HTML'''
            driver.find_element(By.CSS_SELECTOR, 'button.pull-right.mb-xs.mt-xs.mr-xs.btn.btn-primary').click()
            time.sleep(2)
            data        = driver.page_source
            soup        = BeautifulSoup(data , 'html.parser')
    
            '''所有資料共5頁 > 點擊下一頁 並解析 > 將所有資訊疊帶進串列 > 並重複解析'''
            popula = []
            for i in range(5):
                population = soup.select('#datatable')
                for row in population:
                    tds = row.select('td')
                    for td in tds:
                        popula.append(td.text)
                    driver.find_element(By.CSS_SELECTOR, '#datatable_paginate > ul.pagination > li.next > a > span.fa.fa-chevron-right').click()
                    time.sleep(0.3)
                    data        = driver.page_source
                    soup        = BeautifulSoup(data , 'html.parser')
    
            '''_____________對popula串列進行字串處理 > 並設定pd所需要的三大資訊'''
            count       = len(popula)
            Citys       = []
            pop_numbers = []
            index       = str(year) + "年" + str(month) + '月'
            for i in range(count):
                if i % 2 == 0:
                    remove_city_number  = re.sub('\d', '', popula[i])
                    popula[i] = remove_city_number
                    Citys.append(remove_city_number)
                if i % 2 != 0:
                    remove_commas = popula[i].replace("," , "")
                    popula[i] = remove_commas
                    pop_numbers.append(remove_commas)
    
            '''將整理好的字串帶入 >  並帶入原始資料 + 新資料 > 並重複疊帶 > 最後 輸出檔案'''
            df = pd.DataFrame(columns=Citys, index=[index], data=[pop_numbers])
            all_data = pd.concat([all_data, df])
            print(all_data)
    file_name = "新縣市人口統計表99年12月.csv"
    all_data.to_csv(file_name)
    driver.quit()
    print('test2 done')
    
    
'''_______________________________________________使用多工(threading)同步下載'''
t1 = threading.Thread(target = test1)
t2 = threading.Thread(target = test2)
t1.start()
time.sleep(0.5)
t2.start()
t1.join()
t2.join()
print("Done.") 