# test gathered from OpenCV website as their first example https://docs.opencv.org/3.4/da/d22/tutorial_py_canny.html
# used for finding ideal values for the Canny() funciton
import numpy as np
import cv2 as cv
from matplotlib import image, pyplot as plt

imagePath = 'Example2/H01_10_10.jpg'

img = cv.imread(imagePath,0)

x = img.mean(axis=0).mean()
y = img.std()

print('Mean image value: ' + str(x) + '\nStandard Deviation: ' + str(y))