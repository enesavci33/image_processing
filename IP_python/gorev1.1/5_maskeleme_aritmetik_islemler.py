import cv2

def window_close():
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def main():
    img = cv2.imread("../media/06_zongi.jpg")
    img2 = cv2.imread("../media/06_batman.jpg")
    bat_gri=cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)

    cv2.imshow("Zongi",img)
    cv2.imshow("Batman",img2)
    window_close()

    img_h,img_w,img_ch=img2.shape  #h->yükseklik w->geniş"lik  ch->renk kanalı
    roi = img[0:img_h , 0:img_w]

    ret, mask = cv2.threshold(bat_gri, 20, 255, cv2.THRESH_BINARY)
    # mask degiskenine ndarray formatinda maskelenmis resim atanir.
    ters_mask = cv2.bitwise_not(mask)

    sonuc = cv2.add(cv2.bitwise_and(roi, roi, mask=ters_mask), img2)
    img[0:img_h, 0:img_w] = sonuc

    # cv2.imshow("Maske",mask)
    # cv2.imshow("Ters Maske",ters_mask)
    cv2.imshow("Zongi-Batman-Final", img)
    window_close()


if __name__ == "__main__":
    main()
