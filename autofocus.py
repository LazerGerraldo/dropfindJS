# important links https://stackoverflow.com/questions/58314400/edge-detection-for-multiple-images
# uses images in the specified folder directory
# crops images and outputs to cropped
# outputs processed images to a folder Processed

import cv2
import numpy as np
import glob
import matplotlib.pyplot as plt
from numpy.core.fromnumeric import std

procesdVals = []                        # temp array values for standard deviaiton and mean of each picture when looped
avgProcessed = []                       # array of mean values of processed photos
stdProcessed = []                       # array of standard deviation values of processed photos
boxDimen = 500                          # dimension of the cropping box
sourceDir = 'C:/Users/jamie/OneDrive/Shared_Files_Jan_Sci/Autofocus Images/Example12/*.jpg'            # photo source folder
croppedDir = 'Cropped/cropped_{}.png'      # folder for cropped photos to be saved
processedDir = 'Processed/edge_{}.png' # folder for processed photos to be saved 

def sobel(img):
    print('running Sobel')
    sobelX = cv2.Sobel(img, cv2.CV_64F, 1, 0)
    sobelY = cv2.Sobel(img, cv2.CV_64F, 0, 1)
    sobelX = np.uint8(np.absolute(sobelX))
    sobelY = np.uint8(np.absolute(sobelY))

    return cv2.bitwise_or(sobelX, sobelY)

#pass the function an image using format img = cv2.imread('filename')
def auto_crop(img):
    print('cropping images')
    # calculate the cropping values using centered box dimensions
    startRow = (img.shape[0] - boxDimen) // 2
    endRow = (img.shape[0] + boxDimen) // 2
    startCol = (img.shape[1] - boxDimen) // 2
    endCol = (img.shape[1] + boxDimen) // 2

    # Cropping an image
    cropped_image = img[startRow:endRow, startCol:endCol] # cropped = img[start_row:end_row, start_col:end_col]

    # return cv2.GaussianBlur(cropped_image, (3, 3), 0)
    return cropped_image

def plottr(vals):
    plt.plot(vals)
    # plt.title('title')
    plt.xlabel('Image Number')
    plt.ylabel('Standard Deviation Value')
    plt.show()

# Read in each image and convert to grayscale
images = [cv2.imread(file,cv2.IMREAD_GRAYSCALE) for file in glob.glob(sourceDir)]

# Iterate through each image, perform edge detection, and save image
number = 0
for image in images:
    # print('looping')
    crop = auto_crop(image)                             # crop images
    cv2.imwrite(croppedDir.format(number), crop)        # save cropped images in croppedDir
    processed = sobel(crop)                             # process images
    cv2.imwrite(processedDir.format(number), processed) # save processed images in processedDir
    number += 1

    procesdVals = cv2.meanStdDev(processed, mask=None)

    # avgOrig.append(crop.mean(axis=0).mean()) # append mean pixel values for original cropped images
    avgProcessed.append(procesdVals[0][0]) # append mean pixel values for processed images 
    stdProcessed.append(procesdVals[1][0]) # append mean pixel values for processed images 

plottr(stdProcessed)
