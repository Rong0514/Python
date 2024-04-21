import numpy  as np
import matplotlib.pyplot as plt
import seaborn as sns ; sns.set()
'''plt載入中文包'''
plt.rcParams['font.sans-serif']    = ['Microsoft JhengHei'] 
plt.rcParams['axes.unicode_minus'] = False

'''____________________________________________________設定亂樹種子 > 生成數據'''
rng = np.random.RandomState(1)  # 建立一個隨機數生成器，種子值為 1
X   = 10 * rng.rand(50)         # 生成一個包含 50 個介於 0 到 10 之間的隨機數組
y   = 3 * X - 5 + rng.randn(50) # 使用帶有噪音的線性方程生成對應的 y 值

'''________________________________________________________________繪製點散圖'''
plt.scatter(X, y , label = "random = True")

'''__________________________________________________不設定亂樹種子 > 生成數據'''
X   = 10 * rng.rand(50)         # 生成一個包含 50 個介於 0 到 10 之間的隨機數組
y   = 3 * X - 5 + rng.randn(50) # 使用帶有噪音的線性方程生成對應的 y 值

'''________________________________________________________________繪製點散圖'''
plt.scatter(X , y , label = "random = False")


plt.title('亂 樹 種 子 的 差 異')             # 圖標題
plt.xlabel('X')                              # x 軸標籤
plt.ylabel('y')                              # y 軸標籤
plt.legend()    # 輸出label
plt.show()      # 輸出圖片