# important links https://stackoverflow.com/questions/58314400/edge-detection-for-multiple-images
# uses images in the specified folder directory
# crops images and outputs to cropped
# outputs processed images to a folder Processed

import cv2
import numpy as np
import glob
import matplotlib.pyplot as plt

avgOrig = []
avgCanny = []
boxDimen = 650
sourceDir = 'Example2/*.jpg'
croppedDir = 'Cropped/*.png'
processedDir = 'Processed/canny_{}.png'

def auto_canny(image, sigma=0.33):
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

    return cropped_image

# Read in each image and convert to grayscale
images = [cv2.imread(file,0) for file in glob.glob(croppedDir)]

# Iterate through each image, perform edge detection, and save image
number = 0
for image in images:
    # print('looping')
    crop = auto_crop(image)                         # crop images
    cv2.imwrite(croppedDir.format(number), crop)    # save cropped images in croppedDir
    canny = auto_canny(crop)                        # canny images
    cv2.imwrite(processedDir.format(number), canny) # save processed images in processedDir
    number += 1
    
    # avgOrig.append(crop.mean(axis=0).mean()) # append mean pixel values for original cropped images
    avgCanny.append(canny.mean(axis=0).mean()) # append mean pixel values for processed images 

plt.plot(avgCanny) # plotting by columns
# plt.plot(avgOrig) # plotting original image values
plt.title('Processed Image Average Values')
plt.xlabel('Image Index Number')
plt.ylabel('Image Mean Value')
plt.show()


