import cv2 as cv 


'''________________________________________________________________開啟攝像頭'''
cap = cv.VideoCapture(0)

'''_______________________________________________________查攝像頭是否成功開啟'''
if not cap.isOpened():
    print("Cannot open camera")
    exit()


'''___________________________________________進入無限循環，直到按下 'q' 鍵結束'''
while True:

    ret , frame  = cap.read()             # 從攝像頭讀取一幀
    
    cv.imshow("camera", frame)            # 顯示原始圖像
    
    if cv.waitKey(1) & 0xFF == ord("q"):  # 等待按鍵 'q' 鍵，則退出迴圈
        break
    
cap.release()