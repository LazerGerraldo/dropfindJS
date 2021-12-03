# source https://medium.com/simply-dev/what-is-canny-edge-detection-cfefa272a8d0

import cv2
import numpy as np

from matplotlib import pyplot as plt
from numpy.core.fromnumeric import size

source = 'boat.jpg'
blurdir = 'boat_processed_blur.png'
noblurdir = 'boat_processed_no_blur.png'

# takes in a image in the format of cv2.imread("NAME.jpg", cv2.IMREAD_GRAYSCALE)
# and returns a Sobel X and Y processed image
def sobel(img):
    sobelX = cv2.Sobel(img, cv2.CV_64F, 1, 0)
    sobelY = cv2.Sobel(img, cv2.CV_64F, 0, 1)
    sobelX = np.uint8(np.absolute(sobelX))
    sobelY = np.uint8(np.absolute(sobelY))

    return cv2.bitwise_or(sobelX, sobelY)

img = cv2.imread(source, cv2.IMREAD_GRAYSCALE)     # read image using grayscale
blur = cv2.GaussianBlur(img, (3,3), 0)                 # blur image
canny = cv2.Canny(img, 100, 200)                       # basic canny filter

sobelCombined = sobel(img)
sobelBlur = sobel(blur)
# cv2.imwrite(noblurdir, sobelCombined)    # save processed image
# cv2.imwrite(blurdir, sobelBlur)    # save processed image

titles = ['image','blur', 'canny', 'Sobel NO Blur', 'Sobel Blur']
images = [img, blur, canny, sobelCombined, sobelBlur]

# plot all of the images
# for i in range(size(titles)):
#     plt.subplot(2, 3, i+1), plt.imshow(images[i], 'gray')
#     plt.title(titles[i])
#     plt.xticks([]), plt.yticks([])

# plt.show()

array1 = cv2.meanStdDev(sobelCombined, mask=None)
array2 = cv2.meanStdDev(sobelBlur, mask=None)
print('sobel mean and std')
print(array1[0])    # mean pixel values for processed image
print(array1[1])     # standard deviation pixel values for processed image
print('blured sobel mean and std')
print(array2[0])
print(array2[1])    
