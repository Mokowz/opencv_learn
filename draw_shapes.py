import cv2

# Read the image
img = cv2.imread("dickens-lin-FLSbAX8dheQ-unsplash.jpg", 1)

# Width and height
size = 10
width = int(img.shape[1] * size/100)
height = int(img.shape[0] * size/100)
dim = (width, height)

r_img = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)

# Draw the line
img = cv2.line(r_img, (0,0), (640, 480), (20,101,222), 3)
# Arrowed line
img = cv2.arrowedLine(img, (0,480), (640,480), (0, 255, 0), 3)

#Draw rectangle 
img = cv2.rectangle(img, (480, 0), (700, 200), (208,0,0), 5)

# Draw a circle
img = cv2.circle(img, (590, 110), 110, (0, 0, 120), -1)

# Add text
font = cv2.FONT_HERSHEY_SIMPLEX
img = cv2.putText(img, "Cars Day Out", (10, 500), font, 3, (0,210,210), 8)

# Show the image
cv2.imshow("Image", img)

cv2.waitKey(0)
cv2.destroyAllWindows()
