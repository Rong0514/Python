import cv2
import numpy as np

'''__________________________________________________________________讀取圖片'''
img = cv2.imread("lena256rgb.jpg")

'''______________________________________________________________設定仿射矩陣'''

M = np.float32([[1 , 0 , 50] , [0 , 1 , 50]])
'''________________________________________________________M仿射矩陣 細部分解'''
# M = np.float32([[1 ,    #  1 = X 軸長度固定不變，不會進行縮放或拉伸。
#                  0 ,    #  0 = 圖像不會在 X 軸方向發生旋轉，因為旋轉角度為0。
#                  50] ,  #  X 軸向右平移了 50 個像素        
#                 [0 ,    #  1 = Y 軸長度固定不變，不會進行縮放或拉伸。
#                  1 ,    #  0 = 圖像不會在 Y 軸方向發生旋轉，因為旋轉角度為0。
#                  90]])  #  Y軸向下平移了 90 個像素

'''_______________________________________________________取得圖片的高度和寬度'''
print(img.shape) # output > (256 , 256 , 3) > (行數 , 列數 , 3通道RGB)
rows , cols = img.shape[ : 2]

'''___________________________________________透過 warpAffine 函數進行平移變換'''
translation = cv2.warpAffine(img   ,         # 圖檔
                             M     ,         # 仿射矩陣（Affine Matrix）
                             (cols , rows))  # 輸出圖像的大小，也就是所需的寬度和高度。

'''______________________________________顯示圖片 > 任意鍵下一步 > 關閉所有視窗'''
cv2.imshow('Translation', translation)
cv2.waitKey(0)
cv2.destroyAllWindows() 
