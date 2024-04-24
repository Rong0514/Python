import cv2 
import sys

'''______________________________________________嘗試從命令行參數中獲取圖像路徑'''
try:
    imagePath = sys.argv[1]           # 從命令行參數中獲取第一個參數（即圖像路徑）
    image     = cv2.imread(imagePath) # 使用 OpenCV 的 imread 函式讀取圖像
    
    '''_____________________如果無法獲取到命令行參數或讀取圖像失敗，則執行以下操作'''
except:
    image = cv2.imread("lena512rgb.png")

gray         = cv2.cvtColor(image , cv2.COLOR_BGR2GRAY)            # 將圖像轉換為灰階
_ , binary   = cv2.threshold(gray , 127 , 255 , cv2.THRESH_BINARY) # 將灰階圖像二值化

contours, _ = cv2.findContours(binary,                    # 二值化的圖像，只有黑白兩種像素值
                                cv2.RETR_TREE,            # 輪廓檢測模式，建立完整的輪廓階層樹結構
                                cv2.CHAIN_APPROX_SIMPLE)  # 輪廓近似方法，壓縮相鄰的點，節省空間

cv2.imshow("Binary" , binary) # 顯示二值化的圖像
cv2.waitKey(0)

cv2.drawContours(image , contours , -1 , (0 , 255 , 0) , 3) # 繪製圖像中的輪廓

cv2.imshow("Contours" , image) # 顯示帶有檢測到的直線的圖像
cv2.waitKey(0)

'''______________________________________________________________關閉所有視窗'''    
cv2.destroyAllWindows() 
