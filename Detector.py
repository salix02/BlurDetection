#!/bin/env python
# This program takes in an input image name and outputs a 1 if the image is 'blurry' and 0 otherwise.
# A Sobel filter is applied on the grayscale version of the image in both x and y directions individually. The variance
# of the Sobel filtered image is used as the metric for determining blurriness.
# By Joseph Salim

from sys import argv
import cv2

script, img_name = argv

# import image as a grayscale
img = cv2.imread(img_name,0)

# applies a 5x5 sobel filter on the image for the two different directions (x and y) of derivatives
sobelx = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=5)
sobely = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=5)

# finds the variation of the sobel filters
xvar = sobelx.var()
yvar = sobely.var()

# variance threshold for blurry image. A Sobel filtered image with variance on either axis not exceeding this number
# is blurry. Number obtained through experimenting.
threshold = 130000.00

# metric takes the higher value of sobel variance as edges may predominantly exist on either axis
metric = max(xvar,yvar)
print metric

if metric > threshold:
    print "0"
else:
    print "1"





