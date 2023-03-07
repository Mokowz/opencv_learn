import cv2

# Read the image
img = cv2.imread("dickens-lin-FLSbAX8dheQ-unsplash.jpg", 1)

# Draw the line
img = cv2.line(img, (0,0), (640, 480), (20,101,222), 3)

# Show the image
cv2.imshow("Image", img)

cv2.waitKey(0)
cv2.destroyAllWindows()
