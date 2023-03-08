import cv2
import datetime

# Capture the livestream video
cap = cv2.VideoCapture(0)

# Create fourcc variable
fourcc = cv2.VideoWriter_fourcc(*'XVID')

# Output variable (video writer object)
out = cv2.VideoWriter("moii.mp4", fourcc, 30, (640, 480))

# Capture the frames
while(True):
    ret, frame = cap.read()

    if ret == True:

        # write the video
        out.write(frame)

        font = cv2.FONT_HERSHEY_SCRIPT_SIMPLEX
        # text = "Width: "+ str(cap.get(3)) + " Height: " + str(cap.get(4))
        date = str(datetime.datetime.now())
        frame = cv2.putText(frame, date, (10, 40), font, 1, (40,20,231), 2)

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