import pandas as pd


''''歷年月 總人口計算'''

df_data = pd.read_csv('全台灣各縣市-歷年月-人口統計表.csv')

'''年月份'''
df_year_month = df_data['年月'].tolist()

'''每月總人口'''
df_sum = []
for i in range(0 , 313):
    df_popula_sum = df_data.iloc[i , 1:].sum()
    df_sum.append(df_popula_sum)

'''製作表格'''
df_total = pd.DataFrame(columns = ['年月份' , '總人口'])
df_total['年月份'] = df_year_month
df_total['總人口'] = df_sum

# file_name = "歷年月-總人口計算.csv"
# df_total.to_csv(file_name , index = False)

'''___________________________________________________________歷年-人口統計表'''
df_data = pd.read_csv('全台灣各縣市-歷年月-人口統計表.csv')

'''製作 年份 、 各縣市製作'''
years           = [str(i)+'年' for i in range(87, 114)]
columns         = df_data.columns.tolist()
del columns[0]
df_date         = pd.DataFrame(columns= ['年份']+columns)
df_date['年份'] = years  

'''__________________________計算 [各縣市每年人口] 總數據'''
for i in range(87, 114):
    year = str(i)+'年'
    
    '''條件篩選 選擇特定年份的數據'''
    select_date = df_data[df_data['年月'].str.startswith(year)] 
    
    ''' [相加] 各縣市的 整年份的數據'''
    year_total  = select_date.sum()
    del_year    = year_total.tolist()
    del_year    = del_year[1:]
    
    '''將數據依序放進指定的位置'''
    df_date.iloc[i - 87, 1:] = del_year

# file_name = "全台灣各縣市-歷年-人口統計表.csv"
# df_date.to_csv(file_name , index = False)
del columns , del_year , df_data , file_name
del i , select_date , year , year_total , years

'''________________________________________________________各縣市總-人口統計表'''
df_data = pd.read_csv('全台灣各縣市-歷年-人口統計表.csv')

'''製作 各縣市 、 總人口'''
df_total = pd.DataFrame(columns = ['各縣市' , '總人口'])

'''各縣市'''
columns = df_data.columns.tolist()
del columns[0]
df_total['各縣市'] = columns

'''總人口'''
df_data_no_year    = df_data.drop(columns=['年份'])
Total_population   = df_data_no_year.sum()
df_total['總人口']  = Total_population.tolist()

# file_name = "全台灣各縣市-總-人口統計表.csv"
# df_total.to_csv(file_name , index = False)

'''________________________________________________________各年份總-人口統計表'''
df_data  = pd.read_csv('全台灣各縣市-歷年-人口統計表.csv')
df_total = pd.DataFrame(columns = ['年份' , '總人口'])

'''_______________________________年份製作'''
df_year          = df_data['年份'].tolist()
df_year          = [year.replace('年', '') for year in df_year]
df_total['年份'] = df_year

'''_______________________________總人口製作'''
df_popula = df_data.values
'''________________去除年份'''
del_year  = df_popula[:, 1:]
'''________________相加所有人口'''
import numpy as np
del_year           = del_year.astype(float)
sum_popule         = np.sum(del_year, axis=1)
df_total['總人口'] = sum_popule

# file_name = "全台灣各年份-總-人口統計表.csv"
# df_total.to_csv(file_name , index = False)
























