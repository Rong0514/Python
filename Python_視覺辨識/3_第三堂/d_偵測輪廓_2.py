import cv2 
import cv2 as cv 

'''________________________________________________________________開啟攝像頭'''
cap = cv.VideoCapture(0)

'''_______________________________________________________查攝像頭是否成功開啟'''
if not cap.isOpened():
    print("Cannot open camera")
    exit()

'''___________________________________________進入無限循環，直到按下 'q' 鍵結束'''
while True:
    
    ret , frame  = cap.read()                             # 從攝像頭讀取一幀
    gray         = cv.cvtColor(frame , cv.COLOR_BGR2GRAY) # 將幀轉換為灰階
    _ , binary   = cv.threshold(gray , 127 , 255 , cv.THRESH_BINARY) # 將灰階圖像進行二值化處理
    
    contours, _ = cv2.findContours(binary,                    # 二值化的圖像，只有黑白兩種像素值
                                    cv2.RETR_TREE,            # 輪廓檢測模式，建立完整的輪廓階層樹結構
                                    cv2.CHAIN_APPROX_SIMPLE)  # 輪廓近似方法，壓縮相鄰的點，節省空間
    
    cv.imshow("Binary" , binary)                          # 顯示二值化圖像
    cv.drawContours(frame , contours , -1, (0,255,0), 3)  # 繪製輪廓並顯示在原始幀上
    cv.imshow("Contours" , frame)                         # 顯示帶有檢測到的直線的圖像
    
    if cv2.waitKey(1) & 0xFF == ord("q"):                 # 等待按鍵 'q' 鍵，則退出迴圈
        break

'''____________________________________________釋放攝像頭 > 關閉所有OpenCV視窗'''
cap.release()
cv.destroyAllWindows()
