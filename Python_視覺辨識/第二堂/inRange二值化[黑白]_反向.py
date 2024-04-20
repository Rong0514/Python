import cv2
import numpy as np

'''________________________________________載入圖片 > 顯示原始圖 > 任意鍵下一步'''
image = cv2.imread("lena256rgb.jpg")
cv2.imshow("original" , image)
cv2.waitKey(0)


'''_____________________BGR(彩色) 轉換為 HSV 色彩空間 > 顯示HSV圖 > 任意鍵下一步'''
hsv = cv2.cvtColor(image , cv2.COLOR_BGR2HSV)
cv2.imshow("TO_HSV", hsv)
cv2.waitKey(0)


'''___________HSV 值的下界(色相, 飽和度, 明度) > HSV 值的上界(色相, 飽和度, 明度)'''
'''_____________________________________________定義要分離的顏色範圍的下界和上界'''
lower = np.array([141, 0, 130])
upper = np.array([164, 145, 197])

'''_____創建二值化遮罩，其中指定的 HSV 範圍內的像素為白色 (255)，其他像素為黑色 (0)'''
binary = cv2.inRange(hsv , lower , upper)
cv2.imshow("gray_TO_binary" , binary)
cv2.waitKey(0)

'''________________________________________________對二值化遮罩進行位元取反操作'''
bitwise_not = cv2.bitwise_not(binary)
cv2.imshow("binary_TO_bitwise_not" , bitwise_not)
cv2.waitKey(0)


'''___________對原始彩色圖像進行位元取反操作 > 但僅在二值化遮罩中的白色區域進行操作'''
bitwise_not = cv2.bitwise_not(image , mask = binary)
cv2.imshow("binary_TO_bitwise_not > 但只操作白色" , bitwise_not)
cv2.waitKey(0)


'''___________對原始彩色圖像進行位元 AND 運算，僅保留二值化遮罩中的白色區域的像素值'''
bitwise_and = cv2.bitwise_and(image , image , mask = binary)
cv2.imshow("Bitwise_and" , bitwise_and)
cv2.waitKey(0)

cv2.destroyAllWindows()
