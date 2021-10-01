import cv2
import numpy as np
import time
import jetson.inference
import jetson.utils

usb_cap = cv2.VideoCapture(1)

usb_cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
usb_cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

while usb_cap.isOpened():
    print(f'frame: {time.time()}')
    ret, usb_frame = usb_cap.read()
    usb_frame = cv2.cvtColor(usb_frame, cv2.COLOR_BGR2RGB)
    print(usb_frame.shape)
usb_cap.release()
    


