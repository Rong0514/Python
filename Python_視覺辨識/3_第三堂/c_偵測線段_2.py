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
edges = cv2.GaussianBlur(gray, (5, 5), 0)        # 對灰階圖像進行高斯模糊處理
edges = cv2.Canny(gray, 50, 150, 3)              # 使用Canny邊緣檢測算法

print(np.pi/180)

try:
    plines = cv2.HoughLinesP(edges , 1 , np.pi/180 , 50 , None , 100 , 5)
    for pline in plines:
        for pl in pline:
            
            # 使用 cv2.line() 函式在圖像上繪製直線
            # image: 要繪製直線的目標圖像，這裡是我們讀取的原始圖像
            # (pl[0], pl[1]): 直線的第一個端點的坐標，pl[0] 是端點的 x 座標，pl[1] 是端點的 y 座標
            # (pl[2], pl[3]): 直線的第二個端點的坐標，pl[2] 是端點的 x 座標，pl[3] 是端點的 y 座標
            # (255, 0, 0): 直線的顏色，這裡是藍色，因為 (B, G, R) 的元組中藍色值最大，紅色和綠色的值都是零
            # 3: 直線的粗細，表示直線的像素寬度，在這個情況下，直線的寬度為 3 像素
            cv2.line(image, (pl[0], pl[1]), (pl[2], pl[3]), (255, 0, 0), 3)

    cv2.imshow("HoughLinesP", image) # 顯示帶有檢測到的直線的圖像
    cv2.waitKey(0)

except TypeError:
    # 處理當HoughLines函數返回None時的情況
    print("The Houghlines function returns None, try decreasing the threshold!")

'''______________________________________________________________關閉所有視窗'''    
cv2.destroyAllWindows()  

