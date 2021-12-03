# test gathered from OpenCV website as their first example https://docs.opencv.org/3.4/da/d22/tutorial_py_canny.html
# used for finding ideal values for the Canny() funciton
import numpy as np
import cv2
from matplotlib import image, pyplot as plt

# imagePath = 'Cropped/crop_8.png'
imagePath = 'boat.jpg'

img = cv2.imread(imagePath,0)
# edges = cv2.Canny(img,100,200) # default values 100, 200
blurred = cv2.GaussianBlur(img, (3, 3), 0)
edges = cv2.Canny(blurred,10,150) # default values 100, 200
edges2 = cv2.Canny(img,10,150)

# Auto Canny--------------------------------------
v = np.median(img)
sigma = 0.33
# Apply automatic Canny edge detection using the computed median
lower = int(max(0, (1.0 - sigma) * v))
upper = int(min(255, (1.0 + sigma) * v))
auto_canny = cv2.Canny(img, lower, upper)
# Auto Canny--------------------------------------

wide = cv2.Canny(blurred, 10, 200)
tight = cv2.Canny(blurred, 225, 250)


plt.subplot(221),plt.imshow(img,cmap = 'gray')
plt.title('Original Image'), plt.xticks([]), plt.yticks([])
plt.subplot(222),plt.imshow(edges,cmap = 'gray')
plt.title('With Blur'), plt.xticks([]), plt.yticks([])

plt.subplot(223),plt.imshow(edges2,cmap = 'gray')
plt.title('No Blur'), plt.xticks([]), plt.yticks([])
plt.subplot(224),plt.imshow(auto_canny,cmap = 'gray')
plt.title('Auto Canny'), plt.xticks([]), plt.yticks([])

plt.show()