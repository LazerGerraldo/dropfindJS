# uses images in the specified folder directory
# crops images and outputs to cropped
# outputs processed images to a folder Processed

import cv2
import numpy as np
import matplotlib.pyplot as plt

boxDimen = 500                  # bounding box dimension
sourceDir = 'boat.jpg'
croppedDir = 'crop_tiger.png'
processedDir = 'canny_tiger.png'

def auto_canny(image, sigma=0.33): # default sigma=0.33
    # Compute the median of the single channel pixel intensities
    v = np.median(image)
    # print('auto_canny running')

    # Apply automatic Canny edge detection using the computed median
    lower = int(max(0, (1.0 - sigma) * v))
    upper = int(min(255, (1.0 + sigma) * v))
    return cv2.Canny(image, lower, upper)
    # return cv2.Canny(image, 10, 120) # personal parameters if not using above 

#pass the function an image using format img = cv2.imread('filename')
def auto_crop(img):
    # calculate the cropping values using centered box dimensions
    startRow = (img.shape[0] - boxDimen) // 2
    endRow = (img.shape[0] + boxDimen) // 2
    startCol = (img.shape[1] - boxDimen) // 2
    endCol = (img.shape[1] + boxDimen) // 2

    # Cropping an image
    cropped_image = img[startRow:endRow, startCol:endCol] # cropped = img[start_row:end_row, start_col:end_col]

    # return cv2.GaussianBlur(cropped_image, (3, 3), 0)
    return cropped_image

# Read in each image and convert to grayscale
image = cv2.imread(sourceDir,0)

cv2.imshow('original', image)
canny = auto_canny(image)                        # canny images
cv2.imwrite(processedDir, canny) # save processed images in processedDir
cv2.imshow('processed', canny)
cv2.waitKey(0)

cv2.destroyAllWindows()
