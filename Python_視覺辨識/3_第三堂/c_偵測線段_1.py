import cv2
import sys
import numpy as np

'''______________________________________________嘗試從命令行參數中獲取圖像路徑'''
try:
    imagePath = sys.argv[1]           # 從命令行參數中獲取第一個參數（即圖像路徑）
    image     = cv2.imread(imagePath) # 使用 OpenCV 的 imread 函式讀取圖像
    
    '''_____________________如果無法獲取到命令行參數或讀取圖像失敗，則執行以下操作'''
except:
    image = cv2.imread("hough_demo.jpg") # 如果無法從命令列參數中讀取圖像路徑，則使用預設圖像

gray  = cv2.cvtColor(image , cv2.COLOR_RGB2GRAY) # 將圖像轉換為灰階
h , w = gray.shape                               # 獲取灰階圖像的高度和寬度
edges = cv2.GaussianBlur(gray , (5 , 5) , 0)     # 對灰階圖像進行高斯模糊處理
edges = cv2.Canny(gray , 50 , 150 , 3)           # 使用Canny邊緣檢測算法

try:
    # 使用霍夫變換檢測直線
    lines = cv2.HoughLines(edges,            # 二值化圖像，通常是經過 Canny 邊緣檢測處理後得到的
                           1,                # 距離（rho）的精度，以像素為單位的距離解析度
                           np.pi/180,        # 角度（theta）的精度，以弧度為單位的角度解析度
                           250               # 霍夫變換中的閾值參數，用於判斷檢測到的直線的有效性
    )

    # 繪製檢測到的直線
    for line in lines:
        for (rho , theta) in line: # rho 是直線到圖像原點的距離，theta 是直線的角度（以弧度表示）。
            '''_____________________________________________計算直線的兩個端點'''
            x0 = np.cos(theta) * rho 
            y0 = np.sin(theta) * rho
            '''___________________________________________計算直線上的兩個端點'''
            pt1 = (int(x0 + (h + w) * (-np.sin(theta))), int(y0 + (h + w) * np.cos(theta)))
            pt2 = (int(x0 - (h + w) * (-np.sin(theta))), int(y0 - (h + w) * np.cos(theta)))

            cv2.line(image , pt1 , pt2 , (0 , 0 , 255) , 3) # 在原始圖像上繪製直線
 
    
    cv2.imshow("HoughLines" , image) # 顯示帶有檢測到的直線的圖像
    cv2.waitKey(0)

except TypeError:
    # 處理當HoughLines函數返回None時的情況
    print("The Houghlines function returns None, try decreasing the threshold!")

'''______________________________________________________________關閉所有視窗'''    
cv2.destroyAllWindows() 
