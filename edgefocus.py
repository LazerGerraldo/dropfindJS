# 1/5/2021 edgefocus determines the highest standard deviation value of a image
# passed in a folder of jpg images to process, the main will return the name and std value 
# for the most in focus image based on Sobel image processing

import cv2
import numpy as np
import glob

boxDimen = 494                 # dimension of the cropping box for images used in auto_crop()
sourceDir = 'C:/Users/jamie/OneDrive/Shared_Files_Jan_Sci/Autofocus Images/ChrisTest/Compare5/'          # photo source folder end in '/'

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

# takes in an image directory, returns image string and the standard deviation of processed image
def imageprocess(imagedir):
    y = imagedir.split('\\')
    name = y[len(y)-1]                                # crop string to get just image name 
    image = cv2.imread(imagedir,cv2.IMREAD_GRAYSCALE)   # read in the image
    crop = auto_crop(image)                             # crop image
    processed = sobel(crop)                             # process image
    std = cv2.meanStdDev(processed, mask=None)          # calculate standard deviation 
   
    # print(name +' image has a std value value of ' + str(std[1][0]))

    return name, float(std[1][0])

def main(dir):
    # print(imageprocess(imageDir))  # check single image processing

    topimageid = ''
    topimageval = 0

    # loop through all images with .jpg in the passed directory
    for file in glob.glob(dir +'*.jpg'):
        currentimage = imageprocess(file)
        # print(currentimage[0] + ' ' + str(currentimage[1]))

        # if the current image std value surpasses the highest stored std value the new image data is saved
        if currentimage[1] > topimageval: 
            topimageval = currentimage[1]
            topimageid = currentimage[0]
    
    print('the image ' + topimageid + ' had the highest std val of ' + str(topimageval))

main(sourceDir)

