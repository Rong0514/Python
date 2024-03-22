
#%%
'''
_______________________________________________________________________問題檢討
1 . 此[數據]、[特徵數據] 不符合常態分布
2 . 


'''
#%%

import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score
import matplotlib.pyplot as plt
import numpy as np
from sklearn import metrics
import seaborn as sns
from sklearn.preprocessing import StandardScaler

plt.rcParams['font.sans-serif']    = ['Microsoft JhengHei'] 
plt.rcParams['axes.unicode_minus'] = False 

# 讀取數據
data = pd.read_csv('歷年月-總人口計算.csv')

'''_________________________________________________________檢查是否常態性分布'''
sns.pairplot(data)
plt.show()
'''_____________________________________________檢查最直接相關的數據是否常態分布'''
sns.distplot(data['總人口'])
plt.show()

'''____________________________________取特徵'''
X = data['年月份'].values
X = np.arange(1,len(X)+1).reshape(-1,1)
'''____________________________________取目標'''
y = data['總人口'].tolist()

# 將數據劃分為訓練集和測試集
X_train, X_test, y_train, y_test = train_test_split(X  , y ,
                                                    test_size = 0.3 ,
                                                    random_state = 2)

# 創建線性回歸模型對象
model = LinearRegression().fit(X_train, y_train)

y_pred = model.predict(X_test)


'''__________________________________________________________________模型評估'''
# 計算訓練集的r_squared績效
r_squared_train = model.score(X_train,y_train)
print('R_Squared(決定係數) train: ', round(r_squared_train , 2)*100,"%")

# 計算測試集的r_squared績效
r_squared_test = model.score(X_test, y_test)
print('R_Squared(決定係數)  test: ', round(r_squared_test, 2)*100, "%")

# 用測試數據進行預測
r2     = r2_score(y_test, y_pred)
print("R_Squared(決定係數)  test: " , round(r2, 2)*100, "%")

# MAE 是所有實際值與預測值之間的絕對誤差的平均值
# MAE 越小，表示模型的預測能力越好
print('MAE(平均絕對誤差):', metrics.mean_absolute_error(y_test, y_pred))

# MSE 是所有實際值與預測值之間的平方誤差的平均值
# MSE 越小，表示模型的預測能力越好
MSE = np.mean((model.predict(X_test) - y_test) ** 2)
print("MSE(均方誤差)    :", round(MSE, 2))
print('MSE(均方誤差)    :', round(metrics.mean_squared_error(y_test, y_pred) , 2))

# RMSE 是 MSE 的平方根
# RMSE 越小，表示模型的預測能力越好
# RMSE 的優點是它的單位與目標變量的單位相同，因此更容易解釋
print('RMSE(均方根誤差) :', np.sqrt(metrics.mean_squared_error(y_test, y_pred)))

print("截距  :" , model.coef_[0])
print("斜率  :" , model.intercept_ )

'''自行預測'''
print("\n_________________________開始預測__________________________")
year  = eval(input('請輸入預測年份 (民國) : '))
while True:
    month = eval(input('請輸入預測月份 : '))
    if 1 <= month <= 12:
        break
    else:
        print("請輸入正確的年份和月份。月份應該在 1 到 12 之間。")

def index(year , month):
    return (year - 87) * 12 + (month-1)

population_pred = index(year, month)

population_pred = np.array([[population_pred]])

population_pred = model.predict(population_pred)

print("{} 年 {} 月 的預測人口數 : {} 萬人".format(year , month , round(population_pred[0] , 0)))

'''_____________________________________________________________________畫圖'''
plt.figure(figsize=(20, 12)) 
plt.rcParams.update({'font.size' : 20})
plt.scatter(X , y , label='人口增長數據' , s = 5)    
plt.plot(X , model.predict(X) , color='red' , label='測試集預測結果')  
plt.plot(X_test,y_pred,color='red',marker='*',markersize=10)
plt.scatter(index(year, month), population_pred, color='green', marker='*', s=1000, label='預測點')
plt.text(index(year, month) + 0.1, population_pred, f'{round(population_pred[0], 0)} 萬人', fontsize=20, verticalalignment='center')
plt.xticks(np.arange(1, len(X) + 1, 12), np.arange(87, 113+1, 1), rotation=45)
plt.xlabel('年份')
plt.ylabel('人口數')
plt.title('Linear Regression')
plt.grid(True)
plt.legend()
plt.show()

