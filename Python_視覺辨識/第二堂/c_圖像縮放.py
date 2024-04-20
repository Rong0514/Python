import cv2

'''__________________________________________________________________讀取圖片'''
img = cv2.imread("lena256rgb.jpg")

'''_______________________________________________________________顯示原始圖片'''
cv2.imshow('Resize-org', img) 
cv2.waitKey(0)

'''_______________________________________________________取得圖片的高度和寬度'''
print(img.shape) # output > (256 , 256 , 3) > (行數 , 列數 , 3通道RGB)
rows , cols = img.shape[ : 2]

'''___________________________________________透過 cv2.resize 函數進行平移變換'''
'''圖片放大'''
resize = cv2.resize(img ,                             # 原始圖片
                    (int(rows*2) , int(cols*2)) ,     # 將圖片放大兩倍
                    interpolation = cv2.INTER_CUBIC)  # 使用 INTER_CUBIC 插值方法

'''____________________________________________________顯示圖片 > 任意鍵下一步'''
cv2.imshow('Photo_enlarge', resize)
cv2.waitKey(0)

'''圖片縮小'''
resize = cv2.resize(img ,                             # 原始圖片
                    (int(rows*0.5) , int(cols*0.5)) , # 將圖片縮小
                    interpolation = cv2.INTER_CUBIC)  # 使用 INTER_CUBIC 插值方法

'''______________________________________顯示圖片 > 任意鍵下一步 > 關閉所有視窗'''
cv2.imshow('Photo_zoom out', resize)
cv2.waitKey(0)
cv2.destroyAllWindows() 
