import cv2

# Capture the livestream video
cap = cv2.VideoCapture(0)

# Create fourcc variable
fourcc = cv2.VideoWriter_fourcc(*'XVID')

# Output variable (video writer object)
out = cv2.VideoWriter("me.mp4", fourcc, 30, (640, 480))

# Capture the frames
while(True):
    ret, frame = cap.read()

    if ret == True:

        # write the video
        out.write(frame)

        cv2.imshow("webcam", frame)

        # Get the height and width
        # print("Width: ", cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        # print("Height: ", cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

        if cv2.waitKey(1) == ord("q"):
            break
    else:
        break

# Release everything
cap.release()
out.release()
cv2.destroyAllWindows()