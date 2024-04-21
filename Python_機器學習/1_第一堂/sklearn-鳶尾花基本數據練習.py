from sklearn import datasets
import pandas as pd

'''_________________________________從 sklearn 的 datasets 中載入 iris 數據集'''
iris = datasets.load_iris()

print(type(iris))               # 印出 iris 數據集的型態
print(type(iris.data))          # 印出 iris 數據集中的數據的型態
print(type(iris.feature_names)) # 印出 iris 數據集中的特徵名稱的型態
print(iris.feature_names)       # 印出 iris 數據集中的特徵名稱

# y > 目標、標籤
print(iris.target)  # 印出 iris 數據集中的目標值，其中包含了每一朵鳶尾花的種類

'''_____建立 iris_df 新表格 > 資料 = iris.data > 欄位名稱 = iris.feature_names'''
iris_df = pd.DataFrame(iris.data , columns = iris.feature_names)
print(iris_df)

'''_____________________________________________________將 目標 丟給新增的欄位'''
iris_df.loc[: , "species"] = iris.target
# loc         = 建立表格選擇DataFrame的columns和row 
# :           = columns(行)
# "species"   = row(列) 
# iris.target = 將此筆資料給予species這一列
print(iris_df)

iris_df.to_csv("iris_data.csv")
