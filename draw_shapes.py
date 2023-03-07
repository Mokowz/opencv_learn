import cv2

# Read the image
img = cv2.imread("dickens-lin-FLSbAX8dheQ-unsplash.jpg", 1)

# Draw the line
img = cv2.line(img, (0,0), (640, 480), (20,101,222), 3)
# Arrowed line
img = cv2.arrowedLine(img, (0,480), (640,480), (0, 255, 0), 3)

#Draw rectangle 
img = cv2.rectangle(img, (480, 0), (700, 200), (208,0,0), 5)

# Show the image
cv2.imshow("Image", img)

cv2.waitKey(0)
cv2.destroyAllWindows()
