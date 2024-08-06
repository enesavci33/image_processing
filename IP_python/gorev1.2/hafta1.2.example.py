import cv2
import numpy as np
import random

#boş bir görüntü oluştururum 500*500

height,width=750,750

img = np.zeros((height,width,3),dtype=np.uint8)

num_shapes=5

for _ in range(num_shapes):
    shape_type=random.choice(['circle','rectangle'])
    if shape_type=='circle':
        center = (random.randint(0,width),random.randint(0,height))
        radius=random.randint(10,50)
        color=(random.randint(0,255),random.randint(0,255),random.randint(0,255))
        cv2.circle(img,center,radius,color,-1)
    else:
        top_left=(random.randint(0,width),random.randint(0,height))
        bottom_right=(random.randint(top_left[0], width), random.randint(0,top_left[1]))
        color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        cv2.rectangle(img, top_left, bottom_right, color, -1)


#belirtme ksımı
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  #gri resme çevirdim
_, threshold = cv2.threshold(gray, 1, 255, cv2.THRESH_BINARY)  #threshold ile nesneleri beyaz yaptım ve binarye çevirdim.
                                                                         # Sonuç olarak, nesneler beyaz (255) ve arka plan siyah (0) olur.
contours, _ = cv2.findContours(threshold, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
print(contours)
# Nesneleri vurgulamak için konturları çizin
for contour in contours:
    cevre=cv2.arcLength(contour,True)
    alan=cv2.contourArea(contour)
    x, y, w, h = cv2.boundingRect(contour)  # contour u belli olan nesneyi alabilecek en küçük dikdörtgenin koordinat
    epsilon=0.04 * cevre #Yaklaşık çokgen sadeleştirme için kullanılan tolerans değeri. Konturun çevresinin %4'ü olarak belirlenir.
    yaklasik=cv2.approxPolyDP(contour,epsilon,True) #Konturu, epsilon değeri kullanarak sadeleştirir
    if len(yaklasik) == 4:
        shape = "Dikdortgen"
    elif len(yaklasik) > 4:
        shape = "Daire"
    else:
        shape = "Bilinmeyen"
    cv2.drawContours(img, [contour], -1, (0, 255, 0), 2)
    cv2.putText(img, shape, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)


#nesneleri sol kenara en yakın olacak şekilde sıralama

nesne=[]
for contour in contours:
    x,y,w,h=cv2.boundingRect(contour)
    nesne.append((x,y,w,h))

nesne.sort(key=lambda nes:nes[0])

i=1

for yakinlar in nesne:
    #cv2.rectangle(img, (yakinlar[0], yakinlar[1]),(yakinlar[0] + yakinlar[2], yakinlar[1] + yakinlar[3]),(255, 0, 0), 2)
    cv2.putText(img, f"yakin {i}", (yakinlar[0], yakinlar[1] -35),cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)
    i+=1

cv2.imshow('Shapes', img)
cv2.imshow('Shawewpes', gray)
cv2.waitKey(0)
cv2.destroyAllWindows()

