import cv2
def window_close():
    cv2.waitKey(0)
    cv2.destroyAllWindows()

img=cv2.imread("../media/05_600x400.jpg")

img_uzatma = cv2.copyMakeBorder(img,100,100,100,100, cv2.BORDER_REPLICATE)

img_aynalama = cv2.copyMakeBorder(img,250,250,250,250, cv2.BORDER_REFLECT)

img_tekrar = cv2.copyMakeBorder(img,150,150,150,150, cv2.BORDER_WRAP)

img_sarma = cv2.copyMakeBorder(img,25,25,25,25, cv2.BORDER_CONSTANT, value = [0,150,0])

#alan secme
cv2.rectangle(img, (50,120), (140,60), [0,0,200], 2)
#cv2.rectangle(img, 1.nokta, 2.nokta, renk, kalınlık, cizgi tipi)

cv2.imshow("Orijinal",img)
window_close()
cv2.imshow("Uzatma",img_uzatma)
window_close()
cv2.imshow("Aynalama",img_aynalama)
window_close()
cv2.imshow("Tekrar",img_tekrar)
window_close()
cv2.imshow("Sarma",img_sarma)
window_close()
