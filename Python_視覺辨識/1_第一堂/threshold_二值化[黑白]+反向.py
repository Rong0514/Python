import cv2

'''__________________________________________________________________讀取圖片'''
image = cv2.imread('lena256rgb.jpg')
cv2.imshow("Normal" , image)         # show 圖檔
cv2.waitKey(0)                       # 按下按鍵code才會繼續執行 

'''______________________________________________將圖片從 BGR(彩色) 轉換為 灰階'''
gray = cv2.cvtColor(image , cv2.COLOR_BGR2GRAY) 
cv2.imshow("Gray" , gray)            # show 圖檔
cv2.waitKey(0)                       # 按下按鍵code才會繼續執行 

'''_______________________________________使用 cv2.threshold 將 灰階 轉換 黑白'''
ret , Binary_pic = cv2.threshold(gray , # 原始圖片
                                 127  , # 閾值 [[小於127設定成255白色 大於127是黑色]]
                                 255  , # 最大值
                                 cv2.THRESH_BINARY) # 二值化方法（cv2.THRESH_BINARY）
print(ret)
cv2.imshow("Binary" , Binary_pic)
cv2.waitKey(0)
'''
Binary_pic  = 二值化後的圖像
#ret        = 浮點數，代表設置的閾值
0-->255 ('灰階變化') 所以通常取中間值
'''

'''___________________________________________________一灰階 > 黑白 > 黑白相反'''
ret , Binary_INV_pic = cv2.threshold(gray , # 原始圖片
                                     127  , # 閾值 [[小於127設定成255白色 大於127是黑色]]
                                     255  , # 最大值
                                     cv2.THRESH_BINARY_INV)  # 二值化反向方法
print(ret)
cv2.imshow("Binary_INV" , Binary_INV_pic)
cv2.waitKey(0)

'''______________________________________________________________關閉所有視窗'''    
cv2.destroyAllWindows() 