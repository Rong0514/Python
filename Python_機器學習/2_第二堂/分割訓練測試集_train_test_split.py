import numpy as np
from sklearn.model_selection import train_test_split

'''_______________________________________________________________一 維 數 據'''
x1_1d    = np.arange(20)
# print("一 維 數 據 \n",x1)

'''_______________________________________________________________二 維 數 據'''
x1_2d = x1_1d.reshape(-1, 1)
# print("二 維 數 據 \n" , x1_2d)

'''_______________________________________________________________生 成 數 據'''
X = np.arange(20).reshape((10, 2))
y = range(10)
# print(X)
# print(list(y))

'''____________________________________________________________分割訓練測試集'''
X_train, X_test, y_train, y_test = train_test_split(X , # 特徵
                                                    y , # 目標
                                                    test_size    = 0.3, # 取30%當測試集
                                                    random_state = 5)   # 亂樹種子固定

print("X_train value : \n" , X_train , "\n")

print("X_test value : \n"  , X_test  , "\n")

print("y_train value : \n" , y_train , "\n")

print("y_test value : \n"  , y_test)

