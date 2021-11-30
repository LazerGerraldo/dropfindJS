# test gathered from OpenCV website as their first example https://docs.opencv.org/3.4/da/d22/tutorial_py_canny.html
# used for finding ideal values for the Canny() funciton
import numpy as np
import cv2 as cv
from matplotlib import image, pyplot as plt

imagePath = 'Example2/H01_10_10.jpg'

img = cv.imread(imagePath,0)
edges = cv.Canny(img,100,200) # default values 100, 200
edges2 = cv.Canny(img,10,150) 
edges3 = cv.Canny(img,10,120)

plt.subplot(221),plt.imshow(img,cmap = 'gray')
plt.title('Original Image'), plt.xticks([]), plt.yticks([])
plt.subplot(222),plt.imshow(edges,cmap = 'gray')
plt.title('Edge Image 1'), plt.xticks([]), plt.yticks([])

plt.subplot(223),plt.imshow(edges2,cmap = 'gray')
plt.title('Edge Image 2'), plt.xticks([]), plt.yticks([])
plt.subplot(224),plt.imshow(edges3,cmap = 'gray')
plt.title('Edge Image 3'), plt.xticks([]), plt.yticks([])

plt.show()

