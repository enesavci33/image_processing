import cv2

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    frame = cv2.flip(frame, 1)

    if ret == False:
        break

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

    cv2.imshow("Test RGB to GRAY", frame)

cv2.destroyAllWindows()