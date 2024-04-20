import cv2
import sys

'''__________________________________________定義回調函式 > 作用為[軌跡條]的回調'''
def nothing(x):
    pass

"""__________________使用 cv2.namedWindow 創建一個名為 'Gaussian_Blur' 的新視窗"""
cv2.namedWindow('Gaussian_Blur')

'''_________________________________________使用 cv2.createTrackbar 創建軌跡條'''
cv2.createTrackbar('ksize' , 'Gaussian_Blur' , 0 , 10 , nothing)
'''____________________________________________________________軌跡條 細部分解'''
# cv2.createTrackbar('ksize'         , 創建一個名為 'ksize' 的軌跡條
#                    'Gaussian_Blur' , 與 'Gaussian_Blur' 視窗關聯
#                    0               , 軌跡條的初始值為 0
#                    100             , 軌跡條的最大值為 100
#                    nothing         , 指定回調函式 nothing
#                    )

'''______________________________________________嘗試從命令行參數中獲取圖像路徑'''
try:
    imagePath = sys.argv[1]           # 從命令行參數中獲取第一個參數（即圖像路徑）
    image     = cv2.imread(imagePath) # 使用 OpenCV 的 imread 函式讀取圖像
    
    '''_____________________如果無法獲取到命令行參數或讀取圖像失敗，則執行以下操作'''
except:
    image = cv2.imread("lena512rgb.jpg") # 使用預設的圖像 "lena512rgb.png"，並讀取它


while True:
    ksize = cv2.getTrackbarPos('ksize', 'Gaussian_Blur')      # 獲取軌跡條的當前位置（ksize 值）
    blur = cv2.GaussianBlur(image, (2*ksize+1, 2*ksize+1), 0) # 使用高斯模糊處理圖像
    # cv2.resizeWindow('Gaussian_Blur', 500, 500)             # 調整視窗大小
    cv2.imshow('Gaussian_Blur', blur)                         # 顯示高斯模糊後的圖像
    if cv2.waitKey(1) & 0xFF == ord("q"):                     # 等待按鍵 'q' 鍵，則退出迴圈
        break
    
'''______________________________________________________________關閉所有視窗'''    
cv2.destroyAllWindows() 
