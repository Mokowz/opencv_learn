import cv2

# Read the image
img = cv2.imread("dickens-lin-FLSbAX8dheQ-unsplash.jpg", 0)

# print(img)

# Display the image
cv2.imshow("Image", img)
k = cv2.waitKey(0)

if k == 27:
    cv2.destroyAllWindows()
elif k == ord("s"):
    # Write (save the image)
    cv2.imwrite("street.jpg", img)
    cv2.destroyAllWindows()