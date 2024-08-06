import cv2
import numpy as np

cap = cv2.VideoCapture("../media/line.mp4")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.resize(frame, (640, 480))
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lower_yellow = np.array([18, 94, 140], np.uint8)
    upper_yellow = np.array([48, 255, 255], np.uint8)

    mask = cv2.inRange(hsv, lower_yellow, upper_yellow)
    edges = cv2.Canny(mask, 75, 250)

    lines = cv2.HoughLinesP(edges, 1, np.pi / 180, 50, maxLineGap=50)

    if lines is not None:
        for line in lines:
            x1, y1, x2, y2 = line[0]
            cv2.line(frame, (x1, y1), (x2, y2), (200, 0, 200), 5)

    # Orijinal kareyi, maskeyi ve kenarları görüntüleyin
    cv2.imshow("Original Frame", frame)
    cv2.imshow("Mask", mask)
    cv2.imshow("Edges", edges)

    if cv2.waitKey(20) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
