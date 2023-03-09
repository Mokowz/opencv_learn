import cv2
import numpy as np

img = cv2.imread("dickens-lin-FLSbAX8dheQ-unsplash.jpg")

cv2.imshow("Image", img)

# Callback function
def mouse_click(event, x, y, flags, params):
    if event == cv2.EVENT_LBUTTONDOWN:
        font = cv2.FONT_HERSHEY_SCRIPT_SIMPLEX
        strXY = str(x) +  ", " + str(y)
        # strXY = "Love"
        cv2.putText(img, strXY, (x,y), font, .5, (50,210, 100), 2)

        cv2.imshow("Image", img)
    
    if event == cv2.EVENT_RBUTTONDOWN:
        blue = img[y, x, 0]
        green = img[y, x, 1]
        red = img[y, x, 2]
        font = cv2.FONT_HERSHEY_SIMPLEX
        strBGR = str(red) +  ", " + str(green) + ", " + str(blue)
        # strcolor = "Love"
        cv2.putText(img, strBGR, (x,y), font, .5, (42,88, 200), 2)

        cv2.imshow("Image", img)


cv2.setMouseCallback("Image", mouse_click)

cv2.waitKey(0)
cv2.destroyAllWindows()