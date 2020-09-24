import cv2

img = cv2.imread("kalam-veena.jpg")

# Convert the image to gray scale
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Invert the image
inverted_gray_img = 255 - gray_img

# Blur the image by gaussian function
blur_img = cv2.GaussianBlur(inverted_gray_img,(21,21),0)

# inverted the blurred image
inverted_blurred_img = 255 - blur_img

# Create the pencil sketch image
pencil_sketch_IMG = cv2.divide (gray_img, inverted_blurred_img, scale = 256.0)

# Show the image
cv2.imshow('Original Image', img)

cv2.imshow('New Image', pencil_sketch_IMG)

cv2.waitKey(0)

