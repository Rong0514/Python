import cv2
import numpy as np

'''__________________________________________________________________讀取圖片'''
image = cv2.imread("lena256rgb.jpg") 
cv2.imshow("original" , image)
cv2.waitKey(0)

'''______________________________________將圖片從 BGR(彩色) 轉換為 HSV 色彩空間'''
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
cv2.imshow("hsv_pic", hsv)  # 顯示 HSV 圖片
cv2.waitKey(0)              # 等待按鍵以關閉視窗

'''_____________________________________________定義要分離的顏色範圍的下界和上界'''
lower = np.array([141, 0, 0])      # HSV 值的下界 (色相, 飽和度, 明度)
upper = np.array([164, 145, 197])  # HSV 值的上界 (色相, 飽和度, 明度)

'''_____創建二值化遮罩，其中指定的 HSV 範圍內的像素為白色 (255)，其他像素為黑色 (0)'''
binary = cv2.inRange(hsv , lower , upper)
cv2.imshow("Binary", binary) # 顯示二值化黑白圖像
cv2.waitKey(0)               # 等待按鍵以關閉視窗

cv2.destroyAllWindows()      # 關閉所有 OpenCV 視窗