# test gathered from OpenCV website as their first example https://docs.opencv.org/3.4/da/d22/tutorial_py_canny.html

from PIL.Image import Image
import numpy as np
import cv2
from matplotlib import pyplot as plt

def auto_canny(image, sigma=0.33): # default sigma=0.33
    # Compute the median of the single channel pixel intensities
    v = np.median(image)
    # print('auto_canny running')

    # Apply automatic Canny edge detection using the computed median
    lower = int(max(0, (1.0 - sigma) * v))
    upper = int(min(255, (1.0 + sigma) * v))
    return cv2.Canny(image, lower, upper)
    # return cv2.Canny(image, 10, 120) # personal parameters if not using above 

img = cv2.imread('boat.png',0)
# gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# edges = cv.Canny(img,100,200) # skip autocanny
edges = auto_canny(img)
# edges_gray = auto_canny(gray_image)

plt.subplot(221),plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.title('Original Image'), plt.xticks([]), plt.yticks([])
plt.subplot(222),plt.imshow(edges,cmap = 'gray')
plt.title('Edge Image'), plt.xticks([]), plt.yticks([])
# plt.subplot(223),plt.imshow(gray_image,cmap = 'gray')
# plt.title('Gray Image'), plt.xticks([]), plt.yticks([])
# plt.subplot(224),plt.imshow(edges_gray,cmap = 'gray')
# plt.title('Gray Edge Image'), plt.xticks([]), plt.yticks([])

print('Standard Deviation original ' + str(img.std(axis=0).mean())) # standard deviaiton pixel values for original image
print('Standard Deviation edges ' + str(edges.std(axis=0).mean())) # append mean pixel values for processed images 

plt.show()