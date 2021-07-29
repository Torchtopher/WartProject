import numpy as np
import cv2
from mss import mss
from PIL import Image
import pygetwindow
window = "Minecraft 1.8.9"
win = pygetwindow.getWindowsWithTitle(window)[0]

win.size = (1280, 1410)

bounding_box = {'top': 30, 'left': 0, 'width': 1280, 'height': 1400}

sct = mss()
resized = False
while True:
    sct_img = sct.grab(bounding_box)
    cv2.imshow('screen', np.array(sct_img))
    if resized == False:
        win1 = pygetwindow.getWindowsWithTitle("screen")[0]

        win1.size = (1280, 1410)
        resized = True

    if (cv2.waitKey(1) & 0xFF) == ord('q'):
        cv2.destroyAllWindows()
        break