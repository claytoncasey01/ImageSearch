import cv2
import glob
import argparse
import os

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--images", required=True,
                help="Path to the directory that contains the images to be converted")
args = vars(ap.parse_args())

for imagePath in glob.glob(args["images"] + "/*.jpg"):
    imageName = imagePath[imagePath.rfind("/") + 1:]
    image = cv2.imread(imagePath)
    cv2.imwrite(imagePath.replace("jpg", "png"), image)
    if "jpg" in imagePath:
        os.remove(imagePath)
