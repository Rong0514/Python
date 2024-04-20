import cv2
import sys
import numpy as np

'''______________________________________________嘗試從命令行參數中獲取圖像路徑'''
try:
    imagePath = sys.argv[1]           # 從命令行參數中獲取第一個參數（即圖像路徑）
    image     = cv2.imread(imagePath) # 使用 OpenCV 的 imread 函式讀取圖像
    
    '''____________________如果無法獲取到命令行參數或讀取圖像失敗，則執行以下操作'''
except:
    image = cv2.imread("lena512rgb.jpg") # 使用預設的圖像 "lena512rgb.jpg"，並讀取它


'''_____________________________________使用 cv2.cvtColor 將 BRG彩色 轉換 灰階'''
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("Gray", gray)
cv2.waitKey(0)

'''_______________________________________使用 cv2.threshold 將 灰階 轉換 黑白'''
(_ , binary) = cv2.threshold(gray , # 原始圖片
                             127  , # 閾值 [[小於127設定成255白色 大於127是黑色]]
                             255  , # 最大值
                             cv2.THRESH_BINARY) # 二值化方法（cv2.THRESH_BINARY）
cv2.imshow("Binary", binary)
cv2.waitKey(0)

'''___________建立3*3矩陣 > 設定 無符號的8位整數即每個像素的值範圍在 0 到 255 之間'''
kernel = np.ones((3 , 3) , np.uint8) # 

'''_______________________________________使用 cv2.erode 將 黑白圖像 進行 腐蝕'''
erode  = cv2.erode(binary ,        # 黑白圖像
                   kernel ,        # 矩陣
                   iterations = 3) # 腐蝕次數
cv2.imshow("Erode", erode)
cv2.waitKey(0)

'''_______________________________________使用 cv2.dilate 將 黑白圖像 進行 膨脹'''
dilate = cv2.dilate(binary ,       # 黑白圖像
                   kernel ,        # 矩陣
                   iterations = 3) # 膨脹次數
cv2.imshow("Dilate", dilate)
cv2.waitKey(0)

'''______________________________________________________________關閉所有視窗'''    
cv2.destroyAllWindows() 


