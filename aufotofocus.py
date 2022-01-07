# important links https://stackoverflow.com/questions/58314400/edge-detection-for-multiple-images
# uses images in the specified folder directory
# renames the images if not already renamed, saves in a renamed folder
# crops images and outputs to cropped
# outputs processed images to a folder Processed

import cv2
import numpy as np
import os
import glob
import matplotlib.pyplot as plt
import re

procesdVals = []                        # temp array values for standard deviaiton and mean of each picture when looped
avgProcessed = []                       # array of mean values of processed photos
stdProcessed = []                       # array of standard deviation values of processed photos
boxDimen = 494                          # dimension of the cropping box
sourceDir = 'C:/Users/jamie/OneDrive/Shared_Files_Jan_Sci/Autofocus Images/J000972_AF_Temp/Set1/'            # photo source folder end in '/'
croppedDir = sourceDir + 'Cropped/cropped_{}.png'      # folder for cropped photos to be saved
processedDir = sourceDir + 'Processed/edge_{}.png' # folder for processed photos to be saved 

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

# takes in a string and adds a 0 where necessary for later sorting used by method rename()
def addZero(photoid):
    z = photoid.split('\\')             # split the directory into folders and photo name 
    print(photoid)
    y = z[len(z) - 1].split('_')[2] # split to the third set of ID character that should start at 0 and increase by 1
    # y = str(re.search(r'\d+', y).group()) # if the split string contains .jpg or any char values, get jut the integer values
    if (len(y) <= 1):  # if the photo ID only has 1  nonzero didgit, add a 0 before. Ex. _5 becomes _05
        # print('adding 0 before singular digit')
        print('replacing _' + photoid + '_ with _0' + photoid)
        photoid = photoid.replace('_' + y + '_', '_0' + y + '_')

    # y = z[len(z) - 1].split('_') # split photo id into array of strings
    # for breaks in y: # created to add a 0 in front of any single digits in the broke up photo name regardless of photo index location
    #     if (len(breaks) <= 1):  # if the photo ID only has 1  nonzero didgit, add a 0 before. Ex. _5 becomes _05
    #         # print('adding 0 before singular digit')
    #         str = str.replace('_' + y + '_', '_0' + y + '_')
    #         break

    return photoid

# function takes in a directory and changes the image names for sorting uses method addZero()
def rename(xdir):
    flist=sorted(glob.glob(xdir))

    print('updating names')
    # for name in range(len(flist)):
    for name in flist:  # add zeros to file names)
        os.rename(name, addZero(name))

# checks images in source directory have been renamed, looks for empty renamed.txt file in source directory folder
# TODO should not be permanent file names should have correct formatting. Remove rename() and addZero() upon removal of below
def renamecheck():
    if not (glob.glob(sourceDir + 'renamed.txt')): # if rename file does not exist in the renamed folder
        print('txt file does not exist')
        if input('Rename Images? This can NOT be undone. Y/N: ').upper() == 'Y':         # rename images after user confirmation
            # input('Index of singular number 0-14 broken up in the image string? Input number 1-3 ')
            rename(sourceDir+'*.jpg')                          # run rename looking for source images in jpg format in the source directory
            print('saving renamed.txt file')                   # debug message
            # os.mkdir(sourceDir)                               # make the /Renamed folder in the source directory
            renamefile = open(sourceDir + "renamed.txt", "w") # save renamed photos in source/Renamed directory
            renamefile.close()
        else:
            print('Not renaming images, unable to sort')

# plots values of processed images in a simple graph
def plottr(vals):
    global sourceDir
    titledir = sourceDir.split('/')
    plt.plot(vals)
    plt.title(titledir[len(titledir) - 2])
    plt.xlabel('Image Number')
    plt.ylabel('Standard Deviation Value')
    plt.show()

#saves input 2D array 'vals' values to csv file named by input 'filename'
def csvFile(vals, filename):
    excl = open(sourceDir + filename, 'w')
    excl.write('Standard Deviation\n')
    for x in vals:      # loop to each array element
        for y in x:     # loop to each array sub element
            excl.write(str(y)+'\n')

    excl.close()

# checks existence of Cropped/ and Processed/ folders creates if nessary
def startup():
    # Create cropped and processed folders for images to be saved in
    if not (glob.glob(sourceDir + 'Cropped/')):     # if a Cropped/ folder exists don't make a new one
        os.mkdir(sourceDir + 'Cropped/')
        print('Cropped folder did not exist, creating.........')
    if not (glob.glob(sourceDir + 'Processed/')):   # if a Cropped/ folder exists don't make a new one
        os.mkdir(sourceDir + 'Processed/')
        print('Processed folder did not exist, creating.........')

    # renamecheck()                                   # checks if images have been renamed, renames if necessary


def main():
    print('..........running main.......') 
    print('---------- running startup ---------')
    startup() # checking existence of folders and correct naming

    # read in list of image names and sort them
    filesorted = glob.glob(sourceDir+'*.jpg')
    # sort using the integer before jpg in the last 6 chars. ex. A00_00_5.jpg returns 5. see jpgsorting.py
    filesorted = filesorted.sort(key=lambda f: int(re.search(r'\d+', f[len(f)-6:]).group())) 
    print(filesorted)
    # images = [cv2.imread(file,cv2.IMREAD_GRAYSCALE) for file in filesorted]
     
    # TODO don't import all images at once. Instead for each loop
    # convert to grayscale, process, get a value and send the photo ID with the value to csv
    # read in each image and convert to grayscale
    images = [cv2.imread(file,cv2.IMREAD_GRAYSCALE) for file in glob.glob(sourceDir+'*.jpg')]
    # print(images)

 

    # iterate through each image, perform edge detection, and save image
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

    # exit activites of plotting and exporting to a csv file
    csvFile(stdProcessed, 'std.csv') # publish cvs values to a cvs file stored in the same loction as the photos
    # plottr(stdProcessed) # plot the values

main() #run main method
