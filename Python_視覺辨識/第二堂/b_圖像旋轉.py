import cv2

'''__________________________________________________________________讀取圖片'''
img = cv2.imread("lena256rgb.jpg")

'''_______________________________________________________取得圖片的高度和寬度'''
print(img.shape) # output > (256 , 256 , 3) > (行數 , 列數 , 3通道RGB)
rows , cols = img.shape[ : 2]


'''___________________________________________設定getRotationMatrix2D旋轉矩陣'''
M = cv2.getRotationMatrix2D((cols/2 , rows/2) , 45 , scale = 1)
'''________________________________________________________M旋轉矩陣 細部分解'''
# M = cv2.getRotationMatrix2D((rows/2  , 獲取 X 軸 行數中心點
#                              cols/2) , 獲取 Y 軸 列數中心點
#                             45       , 旋轉 45度
#                             scale=1  , 固定縮放因子
#                             )

'''___________________________________________透過 warpAffine 函數進行平移變換'''
rotation = cv2.warpAffine(img      ,         # 圖檔
                             M     ,         # 仿射矩陣（Affine Matrix）
                             (cols , rows))  # 輸出圖像的大小，也就是所需的寬度和高度。

'''______________________________________顯示圖片 > 任意鍵下一步 > 關閉所有視窗'''
cv2.imshow('Rotation' , rotation)
cv2.waitKey(0)
cv2.destroyAllWindows() 