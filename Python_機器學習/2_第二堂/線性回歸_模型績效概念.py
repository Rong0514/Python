import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split

'''_______________________________________________________________一 維 數 據'''
X_1d = np.array([29,28,34,31,25,29,32,31,24,33,25,31,26,30,32,33,34,32])
y_1d = np.array([77,62,93,84,59,64,80,75,58,91,51,73,65,84,82,86,90,85])

'''_______________________________________________________________二 維 數 據'''
X_2d = np.reshape(X_1d , (len(X_1d) , 1))
y_2d = np.reshape(y_1d , (len(y_1d) , 1))
X    = X_2d
y    = y_2d

'''____________________________________________________________分割訓練測試集'''
X_train, X_test, y_train, y_test = train_test_split(X , # 特徵
                                                    y , # 目標
                                                    test_size    = 0.3, # 取30%當測試集
                                                    random_state = 5)   # 亂樹種子固定

'''_______________________________________初始化線性回歸模型， 訓練線性回歸模型'''
#  fit_intercept = 控制模型是否學習截距 > 預設 = True
model_lr = LinearRegression(fit_intercept = True).fit(X_train , y_train)

'''______________________________________________________________使用模型預測'''
y_pred = model_lr.predict(X_test)    # 使用訓練好的模型對測試數據進行預測
# print(y_pred)

'''______________________________________________________________斜率 、 截距'''
print("截距  :" , model_lr.coef_[0][0])    # 輸出模型的斜率
print("斜率  :" , model_lr.intercept_[0])  # 輸出模型的截距

'''_________________________________________________________查看模型訓練的績效'''
MSE       = np.mean((y_pred - y_test)**2) # 計算訓練集的MSE
r_squared = model_lr.score(X_train , y_train)
print("MSE       :" , MSE)
print("r_squared :" , round(r_squared, 4) * 100, "%")

'''
MSE (Mean Squared Error) 是一種衡量模型預測精確度的指標，
    它計算的是預測值與實際值之間差異的平方的平均值。
    較小的 MSE 值表示較低的誤差，即模型的預測結果與實際值更接近。

R-squared（決定係數）是衡量回歸模型解釋變數變異的能力的指標。
    它的值範圍從0到100（百分比形式），其中較高的值表示模型與數據的擬合度更好。
    R-squared 值為 85.7% 表示模型解釋了 85.7% 的變異。
'''

# 繪製線性回歸圖表
plt.scatter(X_1d , y_1d , label = 'Original Data')                       # 原始數據的散點圖
plt.plot(X_test , y_pred , color = 'red' , label = 'Linear Regression')  # 繪製線性回歸模型的預測結果
plt.scatter(X_test , y_pred , color = 'green' , marker = '*' ,
            s = 200 , label = 'Predicted Data')  # 使用星號標記
plt.xlabel('Temperature')        # x軸標籤
plt.ylabel('Iced Tea Sales')     # y軸標籤
plt.title('Linear Regression')   # 圖表標題
plt.legend()                     # 顯示圖例
plt.show()                       # 顯示圖表
