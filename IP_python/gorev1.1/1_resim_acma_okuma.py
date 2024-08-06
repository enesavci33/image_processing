import cv2

img =cv2.imread("C:/Users/MONSTER/Desktop/IP_python/media/05_600x400.jpg",0)
print(type(img)) #img nin tipini öğrendik

cv2.imwrite("C:/Users/MONSTER/Desktop/IP_python/media/600x400_siyah2.jpg", img)

#cv2.imshow("deneme",img)

cv2.waitKey(0)
cv2.destroyAllWindows()