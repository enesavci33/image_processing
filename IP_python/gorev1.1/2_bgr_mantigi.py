import cv2
img = cv2.imread("../media/05_600x400.jpg")
print("img.type : ",type(img)) #numpy.ndarray -> n dimensional(boyutlu) array

print("img.dtype : ",img.dtype) #resmin data tipi -> uint8 -> 8 bitten olusuyor. bu yuzden max 255 degerini alabiliyor.

print("img.shape : ",img.shape) #(yukseklik,genislik,renk kanali sayisi) seklinde cikti verir.

print("img.size : ",img.size) #(yukseklik * genislik * renk kanali) -> resmin kac pikselden olustugunu yazdirir.

#print("img matrisi : ",img) #komutuyla; resmimizin BGR(0-255) karsiliklarini matris seklinde gormekteyiz.

""" fark edildiği üzere fotoğrafın boyutları çok büyük  ve bunlarla çalışmak oldukça zordur.Bu yüzden görüntü işleme 
    uygulamalarında resimlerin boyutlarını düşürerek başlarız.en temel yöntemlerden biri olan resmi siyah beyaz olaraka almaktır.
    yeni sonuçları karşılaştıralım.
"""

img2 = cv2.imread("../media/05_600x400.jpg",0)

print("img.type (siyah-beyaz) : ", type(img2))

print("img.dtype (siyah-beyaz) : ", img2.dtype)

print("img.shape (siyah-beyaz) : ", img2.shape)

print("img.size (siyah-beyaz) : ", img2.size)

cv2.waitKey(0)
cv2.destroyAllWindows()