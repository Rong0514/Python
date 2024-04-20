import cv2

'''__________________________________________________________________讀取圖片'''
image = cv2.imread('lena256rgb.jpg') # 讀取圖檔
cv2.imshow("Normal" , image)         # show 圖檔
cv2.waitKey(0)                       # 按下按鍵code才會繼續執行 

'''______________________________________________將圖片從 BGR(彩色) 轉換為 灰階'''
gray = cv2.cvtColor(image , cv2.COLOR_BGR2GRAY) # 將圖片彩色轉成灰階
cv2.imshow("Gray" , gray)            # show 圖檔
cv2.waitKey(0)                       # 按下按鍵code才會繼續執行  

'''______________________________________________將圖片從 BGR(彩色) 轉換為 HSV'''
hsv = cv2.cvtColor(image , cv2.COLOR_BGR2HSV) # 將圖片BGR(彩色) 轉 HSV
cv2.imshow("HSV" , hsv)
cv2.waitKey(0)

'''______________________________________________將圖片從 HSV 轉換為 BGR(彩色)'''
bgr=cv2.cvtColor(hsv,cv2.COLOR_HSV2BGR) # 將圖片 HSV 轉 BGR(彩色) 
cv2.imshow("BGR" , bgr)
cv2.waitKey(0)

'''______________________________________________________________關閉所有視窗'''    
cv2.destroyAllWindows() 