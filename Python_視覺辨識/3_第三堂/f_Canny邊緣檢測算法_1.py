import cv2 

'''__________________________________________定義回調函式 > 作用為[軌跡條]的回調'''
def nothing(x):
    pass

cv2.namedWindow('canny_demo')                                        # 創建視窗
cv2.createTrackbar('threshold',      'canny_demo', 0, 100, nothing)  # 創建閾值軌跡條
cv2.createTrackbar('increase_ratio', 'canny_demo', 0, 5,   nothing)  # 創建增強比率軌跡條

cap = cv2.VideoCapture(0)  # 捕獲來自攝像頭的影像

while True:
    
    ret , frame = cap.read()                                           # 讀取一幀影像
    threshold   = cv2.getTrackbarPos('threshold'      , 'canny_demo')  # 獲取閾值
    ratio       = cv2.getTrackbarPos('increase_ratio' , 'canny_demo')  # 獲取增強比率
    gray        = cv2.cvtColor(frame , cv2.COLOR_BGR2GRAY)             # 將影像轉換為灰度圖像
    
    edges = cv2.GaussianBlur(gray , (5 , 5) , 0)                                 # 高斯模糊
    edges = cv2.Canny(edges , threshold , threshold * ratio , apertureSize = 3)  # Canny邊緣檢測
    cv2.imshow('canny_demo' , edges)                                             # 顯示Canny邊緣檢測結果

    if cv2.waitKey(1) & 0xFF == ord("q"):     # 等待按鍵 'q' 鍵，則退出迴圈
        cv2.imwrite("canny_demo.png", edges)  # 將處理後的影像儲存為圖像檔
        break

'''____________________________________________釋放攝像頭 > 關閉所有OpenCV視窗'''
cap.release()            # 釋放攝像頭資源
cv2.destroyAllWindows()  # 關閉所有OpenCV視窗
