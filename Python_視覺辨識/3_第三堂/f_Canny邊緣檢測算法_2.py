import cv2
import numpy as np


'''__________________________________________定義回調函式 > 作用為[軌跡條]的回調'''
def nothing(x):
    pass

cap = cv2.VideoCapture(0)  # 捕獲攝像頭影像

while True:
    
    ret , frame = cap.read()       # 讀取一幀影像
    cv2.imshow("preview" , frame)  # 顯示原始影像

    gray = cv2.cvtColor(frame , cv2.COLOR_BGR2GRAY)    # 將影像轉換為灰度圖像
    blurred   = cv2.GaussianBlur(gray , (11 , 11) , 0) # 高斯模糊
    binaryIMG = cv2.Canny(blurred , 20 , 160)          # Canny邊緣檢測
    cnts , _  = cv2.findContours(binaryIMG.copy()  ,
                                 cv2.RETR_EXTERNAL ,
                                 cv2.CHAIN_APPROX_SIMPLE)    # 尋找輪廓
    
    clone = frame.copy()
    cv2.drawContours(clone , cnts , -1 , (0 , 255 , 0) , 2)  # 繪製輪廓
    
    for c in cnts:        
            mask = np.zeros(gray.shape , dtype = "uint8")  # 創建與原始影像相同大小的遮罩
            cv2.drawContours(mask , [c] , -1 , 255 , -1)   # 繪製輪廓到遮罩上
            
            cv2.imshow("Image"        , frame)  # 顯示原始影像
            cv2.imshow("Mask"         , mask)   # 顯示遮罩影像
            cv2.imshow("Image + Mask" , cv2.bitwise_and(frame ,
                                                        frame ,
                                                        mask = mask)) # 將遮罩應用到原始影像上並顯示結果
       
    
    if cv2.waitKey(1) & 0xFF == ord("q"): # 等待按鍵 'q' 鍵，則退出迴圈
        break

'''____________________________________________釋放攝像頭 > 關閉所有OpenCV視窗'''
cap.release()            # 釋放攝像頭資源
cv2.destroyAllWindows()  # 關閉所有OpenCV視窗
