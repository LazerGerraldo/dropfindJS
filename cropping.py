# crop a x length square about the center of the image by using belwo equation
# [(row, column) +/- x] / 2 = (start, end) start and end bounds of cropping
# example (1500, 1000)
# [(1500) +/- 400] / 2 = (550, 950) for row
# [(1000) +/- 400] / 2 = (300, 700) for row
# cropped = img[start_row:end_row, start_col:end_col]

# Import packages
import cv2
import numpy as np
import glob
import matplotlib.pyplot as plt

boxDimen = 650 # size of the cropping box

# img = cv2.imread('Example2/H01_10_10.jpg', 1)

#pass the function an image using format image = cv2.imread('filename')
def Crop(img):
    # print(img.shape) # Print image shape
    cv2.imshow("original", img)

    startRow = (img.shape[0] - boxDimen) // 2
    endRow = (img.shape[0] + boxDimen) // 2
    startCol = (img.shape[1] - boxDimen) // 2
    endCol = (img.shape[1] + boxDimen) // 2

    # Cropping an image
    cropped_image = img[startRow:endRow, startCol:endCol] # cropped = img[start_row:end_row, start_col:end_col]

    return cropped_image

# Read in each image and convert to grayscale
images = [cv2.imread(file,0) for file in sorted(glob.glob("Example2/*.jpg"))]

# Iterate through each image, perform edge detection, and save image
number = 0
for image in images:
    crop = Crop(image)
    cv2.imwrite('Cropped/cropped_{}.png'.format(number), crop)
    number += 1
    # print(image.mean(axis=0).mean())
