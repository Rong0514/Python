import cv2
import sys
import numpy as np

'''__________________________________________定義回調函式 > 作用為[軌跡條]的回調'''
def nothing(x):
    pass

"""_____使用 cv2.namedWindow 創建一個名為 'hsv_demo'的新視窗"""
# cv2.namedWindow('hsv_demo' ,
#                 cv2.WINDOW_NORMAL) # 設定自動調整為與圖像大小相同
cv2.namedWindow('hsv_demo', cv2.WINDOW_NORMAL)  # 創建一個視窗，允許手動調整大小

'''__________________________________________設置初始值為 100，以防止在掩蓋時出錯'''
h , s , v = 100 , 100 , 100

'''_________________________________使用 cv2.createTrackbar 創建[[多個]]軌跡條'''
cv2.createTrackbar('hl', 'hsv_demo', 0,   179, nothing)  # 色相下界
cv2.createTrackbar('hu', 'hsv_demo', 179, 179, nothing)  # 色相上界
cv2.createTrackbar('sl', 'hsv_demo', 0,   255, nothing)  # 飽和度下界
cv2.createTrackbar('su', 'hsv_demo', 255, 255, nothing)  # 飽和度上界
cv2.createTrackbar('vl', 'hsv_demo', 0,   255, nothing)  # 明度下界
cv2.createTrackbar('vu', 'hsv_demo', 255, 255, nothing)  # 明度上界

'''______________________________________________嘗試從命令行參數中獲取圖像路徑'''
try:
    imagePath = sys.argv[1]           # 從命令行參數中獲取第一個參數（即圖像路徑）
    image     = cv2.imread(imagePath) # 使用 OpenCV 的 imread 函式讀取圖像
    
    '''_____________________如果無法獲取到命令行參數或讀取圖像失敗，則執行以下操作'''
except:
    image = cv2.imread("lena256rgb.jpg") # 使用預設的圖像 "lena512rgb.jpg"，並讀取它

while True:
    hl = cv2.getTrackbarPos('hl', 'hsv_demo')# 獲取軌跡條的當前位置（hl 值）
    hu = cv2.getTrackbarPos('hu', 'hsv_demo')# 獲取軌跡條的當前位置（hu 值）
    sl = cv2.getTrackbarPos('sl', 'hsv_demo')# 獲取軌跡條的當前位置（sl 值）
    su = cv2.getTrackbarPos('su', 'hsv_demo')# 獲取軌跡條的當前位置（su 值）
    vl = cv2.getTrackbarPos('vl', 'hsv_demo')# 獲取軌跡條的當前位置（vl 值）
    vu = cv2.getTrackbarPos('vu', 'hsv_demo')# 獲取軌跡條的當前位置（vu 值）

    hsv = cv2.cvtColor(image , cv2.COLOR_BGR2HSV) # 將 BGR 圖像轉換為 HSV 色彩空間

    '''_____________________________________________________使用常規的掩蓋算法'''
    lower = np.array([hl, sl, vl])  # 下界
    upper = np.array([hu, su, vu])  # 上界
    
    '''______________________________________________________________創建掩蓋'''
    mask   = cv2.inRange(hsv , lower , upper)
    '''______________________________________________________________創建掩蓋'''
    result = cv2.bitwise_and(image , image , mask = mask)

    cv2.imshow("hsv_demo", result)        # 顯示圖像

    if cv2.waitKey(1) & 0xFF == ord("q"): # 等待按鍵 'q' 鍵，則退出迴圈
        cv2.imwrite("hsv_demo.png", result)
        break

'''______________________________________________________________關閉所有視窗'''    
cv2.destroyAllWindows() 
