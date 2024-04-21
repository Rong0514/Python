from sklearn import datasets
import matplotlib.pyplot as plt

# 使用make_regression()函數生成隨機的回歸問題數據集
X , y = datasets.make_regression(n_samples     = 100,
                                 n_features    = 1  ,
                                 n_informative = 1  , 
                                 n_targets     = 1  ,
                                 noise         = 7  ,
                                 shuffle       = False ,
                                 random_state  = 5  ,  )
plt.scatter(X , y)
plt.show
'''
# 以下是一些可選參數,用於控制生成數據集的特徵:
# n_samples     : 生成的樣本數量        ，預設為100
# n_features    : 每個樣本的特徵數量    ，預設為100 
# n_informative : 真實相關特徵的個數    ，預設為10
# n_targets     : 指定生成的目標值的數量，預設為1
# noise         : 加入的高斯雜訊水平    ，預設為0.1
# shuffle       : 是否打亂數據順序      ，預設為False
# random_state  : 亂數種子固定實驗結果  ，預設為0
'''