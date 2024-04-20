import cv2 # cv2 = open-cv
import numpy as np

# 指定 NumPy 陣列的數據類型為無符號的8位整數（unsigned 8-bit integer）。
green     = np.array([[[0 , 255 , 0]]] , dtype = 'uint8') 

hsv_green = cv2.cvtColor(green , cv2.COLOR_BGR2HSV)
# 使用OpenCV中的cv2.cvtColor函數將RGB格式的顏色轉換為[[HSV]]格式。
# cv2.COLOR_BGR2HSV，表示從BGR格式（Blue-Green-Red，與RGB相反）轉換為[[HSV]]格式。

print(hsv_green)

'''_____________________________________為什麼像素顏色值表示需要使用三維陣列呢？'''
# '''
# 這個問題的要點主要在於圖像處理中的顏色表示方式和資料結構。

# 顏色通道：
#     在圖像處理中，通常使用紅色（R）、綠色（G）、藍色（B）三個基本色彩通道來表示顏色。
#     每個像素的顏色都可以通過這三個通道的數值來表示，分別代表了紅色、綠色和藍色的強度。
#     因此，為了完整地表示一個像素的顏色，需要有三個數字來分別表示這三個通道的值。
    
# 資料結構：
#     在NumPy中，多維陣列是用於表示多維資料的一種有效方式。
#     對於像素顏色值來說，可以使用三維的NumPy陣列來表示。
#     其中，第一個維度表示像素的行數，第二個維度表示像素的列數，而第三個維度則表示色彩通道。
#     因此，使用三維陣列可以很自然地表示像素的顏色值，每個像素對應一個三維的數值，分別表示了紅色、綠色和藍色通道的值。
    
# 總的來說，像素顏色值需要使用三維陣列表示是因為圖像處理中的顏色表示方式和資料結構的特點，
# 其中每個像素的顏色需要使用三個數字來表示，而使用三維陣列可以很好地符合這一需求。
# '''

'''_______為甚麼opencvRGB[[[0, 255, 0]]]轉換HSV後[[[ 60 255 255]]]為甚麼是60??'''
# '''
# 在OpenCV中，HSV色彩空間的H（色調）值的範圍是0到179，而不是通常的0到360。
# 這是因為在OpenCV中，H值被縮放到一個範圍內，以使其適合8位數據類型（unsigned 8-bit integer）。

# 對於一般的HSV色彩空間，色調值（H）表示顏色的種類或色相，0對應於紅色，60對應於黃色，120對應於綠色，以此類推。
# 因此，綠色在HSV色彩空間中的色調值應該是60。

# 在這個例子中，將RGB顏色[0, 255, 0]轉換為HSV色彩空間後，綠色的色調值應該是60。
# 所以，轉換後的結果中，色調值為60是正確的。
# '''