# import the necessary packages
from imutils import paths
import argparse
import cv2


def variance_of_laplacian(image):
    # compute the Laplacian of the image and then return the focus
    # measure, which is simply the variance of the Laplacian
    return cv2.Laplacian(image, cv2.CV_64F).var()


# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--images", required=True,
                help="path to input directory of images")
ap.add_argument("-t", "--threshold", type=float, default=100.0,
                help="focus measures that fall below this value will be considered 'blurry'")
args = vars(ap.parse_args())

counter = 0

# loop over the input images
for imagePath in paths.list_images(args["images"]):
    # load the image, convert it to grayscale, and compute the
    # focus measure of the image using the Variance of Laplacian
    # method
    image = cv2.imread(imagePath)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    #fm = variance_of_laplacian(gray)
    #laplacian = cv2.Laplacian(gray, cv2.CV_64F).mean()

    sobelx = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=5)
    sobely = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=5)

    thresh = 127
    imx = cv2.threshold(sobelx, thresh, 255, cv2.THRESH_BINARY)[1]
    imy = cv2.threshold(sobely, thresh, 255, cv2.THRESH_BINARY)[1]

    text = "Blurry"

    threshold = 130000.00

    xvar = sobelx.var()
    yvar = sobely.var()

    # if the focus measure is less than the supplied threshold,
    # then the image should be considered "blurry"

    metric = max(xvar,yvar)
    if (metric) > threshold:
        text = "Not Blurry"
        counter = counter + 1



    #print "xvar = %.2f yvar = %.2f xmean = %.2f ymean = %.2f %s %s" % (xvar, yvar, sobelx.mean(), sobely.mean(), imagePath, text)

print counter
