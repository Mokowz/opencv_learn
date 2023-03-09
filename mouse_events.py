import cv2
import numpy as np

# img = cv2.imread("dickens-lin-FLSbAX8dheQ-unsplash.jpg")
img = np.zeros([512,512,3], np.uint8)
points = []
cv2.imshow("Image", img)

# Callback function
def mouse_click(event, x, y, flags, params):
    # Create a lnie between two points
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img, (x,y), 3, (0,200,40), -1)
        points.append((x,y))

        if len(points) >= 2:
            cv2.line(img, points[-1], points[-2], (120,250, 50), 3)
        

    if event == cv2.EVENT_RBUTTONDOWN:
        font = cv2.FONT_HERSHEY_SIMPLEX
        text = "Done"
        cv2.putText(img, text, (x,y), font, 1, (0,0,255), 2)
    
    cv2.imshow("Image", img)
    
    


cv2.setMouseCallback("Image", mouse_click)

cv2.waitKey(0)
cv2.destroyAllWindows()