import cv2

cap = cv2.VideoCapture(0)

ret,frame = cap.read()
while(True):
    cv2.imshow('frame',frame)
    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        break
    if key == ord('s'):
        path = "photo.jpg"
        cv2.imwrite(path,frame)

cap.release()
cv2.destroyAllWindows()
