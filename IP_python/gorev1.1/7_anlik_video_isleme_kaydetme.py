import cv2
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW) #dahili webcam için 0, farklı cam için 1, var olan video için dosya yolu

outName="EnesTest.mp4"
codec=cv2.VideoWriter_fourcc('M', 'P', '4', '2')
frameRate = 10 #saniyede 10 kare kayı
resolution = (640, 480)
videoOutput = cv2.VideoWriter(outName, codec, frameRate, resolution)

while True:
    ret, frame = cap.read()
    #var olan bir video işlenecekse 'if ret==0: break' eklanmeli. sonsuz döngüden kaçınmak için.

    frame = cv2.flip(frame, 1) #videoyu y eksenli aynalamak için.. x ekseni için -1..
    videoOutput.write(frame)
    cv2.imshow("Live Cam", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"): # her frame'i 1 ms göster, q ile çık..
    #cam fps değerine göre ideal bir değer ayarlanmalı.
        break

videoOutput.release()
cap.release()
cv2.destroyAllWindows()