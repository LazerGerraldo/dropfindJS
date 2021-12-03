# importing the opencv(cv2) module
import cv2
# reading the image
image = cv2.imread('boat.png')
# changing the color space
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# showing the resultant image
cv2.imshow('Grayscale Lion', gray_image)
# waiting until key press
cv2.waitKey()
# destroy all the windows
cv2.destroyAllWindows()