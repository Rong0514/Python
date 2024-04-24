import cv2 
import sys

'''__________________________________________定義回調函式 > 作用為[軌跡條]的回調'''
def nothing(x):
    pass

cv2.namedWindow('canny_demo')
cv2.createTrackbar('threshold'      , 'canny_demo' , 0 , 100 , nothing)
cv2.createTrackbar('increase_ratio' , 'canny_demo' , 0 , 5   ,   nothing)

'''______________________________________________嘗試從命令行參數中獲取圖像路徑'''
try:
    imagePath = sys.argv[1]           # 從命令行參數中獲取第一個參數（即圖像路徑）
    image     = cv2.imread(imagePath) # 使用 OpenCV 的 imread 函式讀取圖像
    
    '''_____________________如果無法獲取到命令行參數或讀取圖像失敗，則執行以下操作'''
except:
    image = cv2.imread("lena512rgb.png") # 使用預設的圖像 "lena512rgb.png"，並讀取它

while True:
    threshold = cv2.getTrackbarPos('threshold' ,      'canny_demo')# 獲取軌跡條的當前位置（threshold 值）
    ratio     = cv2.getTrackbarPos('increase_ratio' , 'canny_demo')# 獲取軌跡條的當前位置（increase_ratio 值）

    gray  = cv2.cvtColor(image , cv2.COLOR_BGR2GRAY)               # 將圖像轉換為灰階
    edges = cv2.GaussianBlur(gray   ,  # 要處理的灰階圖像
                             (5, 5) ,  # 高斯核的大小，此處為 5x5
                             0      ,  # 高斯核在 X 方向的標準差，此處設定為 0，表示自動計算標準差
    )                                  # 對灰階圖像進行高斯模糊處理
    
    '''______________________________________________________執行Canny邊緣檢測'''
    edges = cv2.Canny(edges             ,           # 原始圖像
                      threshold         ,           # 用於檢測邊緣的閾值
                      threshold * ratio ,           # 高閾值為低閾值的倍數
                      apertureSize = 3  ,           # Sobel算子的大小，影響梯度計算[只有3 5 7可選擇]
    ) 
    cv2.imshow('canny_demo' , edges)                # 顯示圖像
   
    bit_and = cv2.bitwise_and(image , image , mask = edges) # 使用位元運算來將Canny邊緣檢測的結果應用到原始圖像上
    cv2.imshow('canny_and' , bit_and)               # 顯示圖像
    
    if cv2.waitKey(1) & 0xFF == ord("q"):    # 等待按鍵 'q' 鍵，則退出迴圈
        cv2.imwrite("canny_demo.png", edges) # 將Canny邊緣檢測後的圖像儲存為PNG格式
        break                                # 中斷迴圈

'''______________________________________________________________關閉所有視窗'''    
cv2.destroyAllWindows() 

