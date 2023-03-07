import cv2

# Capture the livestream video
cap = cv2.VideoCapture(0)

# Capture the frames
while(True):
    ret, frame = cap.read()

    cv2.imshow("webcam", frame)

    if cv2.waitKey(1) == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()