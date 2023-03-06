import cv2

# Read the image
img = cv2.imread("dickens-lin-FLSbAX8dheQ-unsplash.jpg", 0)

# print(img)

# Display the image
cv2.imshow("Image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()