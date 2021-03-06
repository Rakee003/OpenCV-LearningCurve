# -*- coding: utf-8 -*-
"""
Created on Sat Jul 17 17:22:52 2021

@author: Rakesh Kumar
"""

# Import the required packages
import cv2
import time



# We create a VideoCapture object to read from the camera (pass 0):
capture = cv2.VideoCapture(0)

# Get some properties of VideoCapture (frame width, frame height and frames per second (fps)):
frame_width = capture.get(cv2.CAP_PROP_FRAME_WIDTH)
frame_height = capture.get(cv2.CAP_PROP_FRAME_HEIGHT)
fps = capture.get(cv2.CAP_PROP_FPS)

# Print these values:
print("CV_CAP_PROP_FRAME_WIDTH: '{}'".format(frame_width))
print("CV_CAP_PROP_FRAME_HEIGHT : '{}'".format(frame_height))
print("CAP_PROP_FPS : '{}'".format(fps))

# Check if camera opened successfully
if capture.isOpened()is False:
    print("Error opening the camera")

# Read until the video is completed, or 'q' is pressed
while capture.isOpened():
    # Capture frame-by-frame from the camera
    ret, frame = capture.read()

    if ret is True:
        # Calculate time before processing the frame:
        processing_start = time.time()

        # Display the captured frame:
        cv2.imshow('Input frame from the camera', frame)

        # Convert the frame captured from the camera to grayscale:
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Display the grayscale frame:
        cv2.imshow('Grayscale input camera', gray_frame)

        # Press q on keyboard to exit the program:
        if cv2.waitKey(20) & 0xFF == ord('q'):
            break

        # Calculate time after processing the frame:
        processing_end = time.time()

        # Calculate the difference:
        processing_time_frame = processing_end - processing_start

        # FPS = 1 / time_per_frame
        # Show the number of frames per second:
        print("fps: {}".format(1.0 / processing_time_frame))

    # Break the loop
    else:
        break
 
# Release everything:
capture.release()
cv2.destroyAllWindows()