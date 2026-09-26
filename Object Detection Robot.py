# Object Detection Robot using Python

# Install required libraries:

# pip install opencv-python

import cv2

# Start camera

camera = cv2.VideoCapture(0)

# Load pre-trained object detection model

net = cv2.dnn.readNetFromCaffe(
"MobileNetSSD_deploy.prototxt",
"MobileNetSSD_deploy.caffemodel"
)

# Object classes

classes = [
"background", "aeroplane", "bicycle", "bird",
"boat", "bottle", "bus", "car", "cat",
"chair", "cow", "diningtable", "dog",
"horse", "motorbike", "person", "pottedplant",
"sheep", "sofa", "train",
