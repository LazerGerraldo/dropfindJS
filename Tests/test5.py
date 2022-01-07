# testing sorting of images based on the timestamp or
#  final set of numbers in the *.jpg

import glob
import re
import cv2
import numpy as np

boxDimen = 495 # bounding box dimension for photo cropping used in auto_crop()
stdProcessed = []

sourceDir = 'C:/Users/jamie/OneDrive/Shared_Files_Jan_Sci/Autofocus Images/J000972_AF_Temp/Set1/*.jpg'            # photo source folder end in '/'
flist=glob.glob(sourceDir)

# takes in a grayscale image initialized with cv2, and returns a processed image using Sobel XY processing
def sobel(img):
    # print('running Sobel')
    sobelX = cv2.Sobel(img, cv2.CV_64F, 1, 0)
    sobelY = cv2.Sobel(img, cv2.CV_64F, 0, 1)
    sobelX = np.uint8(np.absolute(sobelX))
    sobelY = np.uint8(np.absolute(sobelY))

    return cv2.bitwise_or(sobelX, sobelY)

# pass the function an image using format img = cv2.imread('filename')
# see cropping.py for more info
def auto_crop(img):
    # print('cropping images')
    # calculate the cropping values using centered box dimensions
    startRow = (img.shape[0] - boxDimen) // 2
    endRow = (img.shape[0] + boxDimen) // 2
    startCol = (img.shape[1] - boxDimen) // 2
    endCol = (img.shape[1] + boxDimen) // 2

    # Cropping an image
    cropped_image = img[startRow:endRow, startCol:endCol] # cropped = img[start_row:end_row, start_col:end_col]

    # return cv2.GaussianBlur(cropped_image, (3, 3), 0)
    return cropped_image

#saves input 2D array 'vals' values to csv file named by input 'filename'
def csvFile(vals, filename):
    excl = open(filename, 'w')
    excl.write('Standard Deviation\n')
    for x in vals:      # loop to each array element
        for y in x:     # loop to each array sub element
            excl.write(str(y)+'\n')

    excl.close()

# sort the list of images
#----------DO NOT DELETE--------------------------------------------------------------    
flist.sort(key=lambda f: int(re.search(r'\d+', f[len(f)-6:]).group()))
#----------DO NOT DELETE--------------------------------------------------------------

images = [cv2.imread(file,cv2.IMREAD_GRAYSCALE) for file in flist]

procesdVals = []
for image in images:
    # print(y)
    # print('looping')
    crop = auto_crop(image)                             # crop images
    processed = sobel(crop)                             # process images

    procesdVals = cv2.meanStdDev(processed, mask=None)
    stdProcessed.append(procesdVals[1][0]) # append mean pixel values for processed images 

csvFile(stdProcessed, 'C:/Users/jamie/OneDrive/Shared_Files_Jan_Sci/Autofocus Images/J000972_AF_Temp/Set1/std.csv')
