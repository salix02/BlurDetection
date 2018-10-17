#!/bin/env python

from sys import argv
import cv2
from matplotlib import pyplot as plt


#def variance_of_laplacian(image):
    #return cv2.Laplacian(image, cv2.CV_64F).var()


script, img_name = argv

#img_name = '20170427T163322_G0029277.JPG'


img = cv2.imread(img_name,0)

#lapVar = cv2.Laplacian(img, cv2.CV_64F).var()

#if lapVar < 100:
#    print 0
#else:
#    print 1

#print lapVar


sobelx = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=-1)
sobely = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=-1)

thresh = 127
imx = cv2.threshold(sobelx, thresh, 255, cv2.THRESH_BINARY)[1]
imy = cv2.threshold(sobely, thresh, 255, cv2.THRESH_BINARY)[1]


plt.subplot(2, 2, 1), plt.imshow(img, cmap='gray')
plt.title('Original'), plt.xticks([]), plt.yticks([])
plt.subplot(2,2,3),plt.imshow(imx, cmap='gray')
plt.title('Sobel X'), plt.xticks([]), plt.yticks([])
plt.subplot(2,2,4),plt.imshow(imy, cmap='gray')
plt.title('Sobel Y'), plt.xticks([]), plt.yticks([])


plt.show()

