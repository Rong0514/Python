import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

'''_________________________________________________________________________________________________________________________'''
# df_month = pd.read_csv('全台灣各縣市-歷年月-人口統計表.csv')
# '''載入中文包'''
# plt.rcParams['font.sans-serif']    = ['Microsoft JhengHei'] 
# plt.rcParams['axes.unicode_minus'] = False 

# '''設定各縣市固定顏色'''
# city_colors = {
#     '臺北市': 'blue','新北市': 'orange',
#     '臺中市': 'green','臺南市': 'red','高雄市': 'purple','宜蘭縣': 'brown',
#     '桃園市': 'pink','新竹市': 'gray','新竹縣': 'olive','苗栗縣': 'cyan',
#     '彰化縣': 'magenta','南投縣': 'lime','雲林縣': 'teal','嘉義市': 'coral',
#     '嘉義縣': 'gold','屏東縣': 'navy','臺東縣': 'sienna','花蓮縣': 'orchid',
#     '澎湖縣': 'peru','基隆市': 'khaki','金門縣': 'indigo','連江縣': 'deeppink'
# }

# '''設定圖片儲存路徑'''
# path = r"C:\Users\willy\OneDrive\桌面\Python-機器學習-視覺辨識\自主練習-機器學習-台灣人口預測\全台灣各縣市-歷年月-人口統計表"

# '''繪製歷年月的值線圖 _ 分析各縣市人口變動趨勢'''
# for index in range(0 , 313):

#         '''抓取 人口數'''
#         data              = df_month.iloc[index , :]
#         population        = data[1:].tolist()
                
#         '''抓取 各縣市'''
#         city = df_month.columns.tolist()[1:]
        
#         '''排序 人口數 、 各縣市'''
#         population_sorted , city_sorted = zip(*sorted(zip(population , city) , reverse=True))

#         # 設置全局字體大小
#         plt.rcParams.update({'font.size' : 30})
#         # 創建新的圖形，指定尺寸為 30x18 英寸
#         plt.figure(figsize=(30, 18))
#         # 根據城市排序後的顏色列表
#         colors = [city_colors[city] for city in city_sorted]
#         # 繪製水平條形圖，城市為y軸，人口數量為x軸，並根據城市對應的顏色進行著色
#         plt.barh(city_sorted, population_sorted, color=colors)
#         # 設置圖形標題，以年月作為標題的一部分
#         plt.title('台灣各地區人口 - {}'.format(df_month.iloc[index]['年月']))
#         # 設置y軸標籤為地區
#         plt.ylabel('地區')
#         # 設置x軸標籤為人口
#         plt.xlabel('人口')
#         # 設置x軸刻度的範圍和步長
#         x_min, x_max = plt.xlim()                          
#         step = 500000                             
#         xtick_locs = np.arange(0, x_max, step)          
#         xtick_labels = [f'{x//1000}K' for x in xtick_locs] 
#         plt.xticks(xtick_locs, xtick_labels)               
#         # 反轉y軸方向，使得人口數量大的城市在上方
#         plt.gca().invert_yaxis()
#         # 在長條圖後面添加數據
#         for i, (city, population) in enumerate(zip(city_sorted, population_sorted)):
#             plt.text(population, i, f'{population//1000}K', va='center', fontsize=35)
#         # 組合圖片的檔案路徑，包含路徑和年月的信息
#         file_path = os.path.join(path, '台灣各地區人口-{}.png'.format(df_month.iloc[index]['年月']))
#         # 將圖形保存為PNG文件，並使用bbox_inches='tight'參數確保保存的圖形不會被裁切
#         plt.savefig(file_path, bbox_inches='tight')
#         # 顯示圖形
#         plt.show()
'''_________________________________________________________________________________________________________________________'''

# df_total      = pd.read_csv('全台灣各縣市-總-人口統計表.csv')

# '''載入中文包'''
# plt.rcParams['font.sans-serif']    = ['Microsoft JhengHei'] 
# plt.rcParams['axes.unicode_minus'] = False 

# '''排序總人口數'''
# df_total   = df_total.sort_values(by='總人口', ascending=False)

# '''抓取各縣市 、 總人口'''
# city       = df_total['各縣市'].tolist()
# population = df_total['總人口'].tolist() 

# '''計算比例'''
# total_population      = sum(population)  
# population_percentage = [(pop / total_population) * 100 for pop in population]

# plt.rcParams.update({'font.size' : 35})
# plt.figure(figsize=(30, 18))                             # 創建一個圖形窗口，設置大小為10x6
# plt.barh(city, population_percentage, color='skyblue')  # 創建水平條形圖，用藍色表示，x軸為各縣市，y軸為人口比例
# plt.gca().invert_yaxis()                                # 反轉y軸，使得人口比例從高到低排列
# plt.title('各縣市總人口比例')                            # 設置標題
# plt.ylabel('地區')                                      # 設置y軸標籤
# plt.xlabel('人口比例 (%)')                              # 設置x軸標籤為人口比例（百分比）
# for i in range(len(city)):
#     plt.text(population_percentage[i], i, f'{population_percentage[i]:.2f}%', ha='left', va='center')
# plt.show() 

