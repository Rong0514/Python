import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns; sns.set()
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

'''____________________________________________________設定亂樹種子 > 生成數據'''
rng = np.random.RandomState(1)  # 建立一個隨機數生成器，種子值為 1
X   = 10 * rng.rand(50)         # 生成一個包含 50 個介於 0 到 10 之間的隨機數組
y   = 3 * X - 5 + rng.randn(50) # 使用帶有噪音的線性方程生成對應的 y 值
# print(X)
# print(y)
X   = X.reshape(-1, 1)          # 將特徵 X 轉換成二維數組
# print(X)

'''____________________________________________________________分割訓練測試集'''
X_train, X_test, y_train, y_test = train_test_split(X , # 特徵
                                                    y , # 目標
                                                    test_size    = 0.3, # 取30%當測試集
                                                    random_state = 5)   # 亂樹種子固定

'''__初始化線性回歸模型，fit_intercept = 控制模型是否學習截距 > 訓練線性回歸模型'''
model  = LinearRegression(fit_intercept = True).fit(X_train, y_train)

'''______________________________________________________________使用模型預測'''
y_pred = model.predict(X_test)    # 使用訓練好的模型對測試數據進行預測

'''_____________________________________________________繪製數據和模型預測結果'''
plt.scatter(X , y)                           # 繪製原始數據的散點圖
plt.plot(X_test , y_pred , color = 'red' ,
         label = 'Linear Regression' , linewidth = 1) # 繪製線性回歸模型的預測結果

plt.scatter(X_test , y_pred , color = 'green' , marker = '*' ,
            s = 200 , label = 'Predicted Data')  # 使用星號標記，並且將顏色設置為綠色
plt.xlabel('X')                              # x 軸標籤
plt.ylabel('y')                              # y 軸標籤
plt.title('Linear Regression')               # 圖標題

'''______________________________________________________________斜率 、 截距'''
print("截距  :" , model.coef_[0])    # 輸出模型的斜率
print("斜率  :" , model.intercept_)  # 輸出模型的截距
