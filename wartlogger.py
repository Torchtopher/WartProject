import mss
import win32gui
import os
import time
from datetime import datetime
import cv2
from PIL import Image
import numpy as np
import pyautogui
pythonpath = r"C:\Users\choll\AppData\Local\Programs\Python\Python39\python.exe"
try:
	hwnd = win32gui.FindWindow(None, pythonpath)

	x0, y0, x1, y1 = win32gui.GetWindowRect(hwnd)
	w = x1 - x0 # width
	h = y1 - y0 # height

	win32gui.MoveWindow(hwnd, 1255, 480, 1315, 495, True)
	#BGR NOT RGB
except:
	hwnd = win32gui.FindWindow(None, "Command Prompt - wartlogger.py")

	x0, y0, x1, y1 = win32gui.GetWindowRect(hwnd)
	w = x1 - x0 # width
	h = y1 - y0 # height

	win32gui.MoveWindow(hwnd, 1255, 500, 1315, 480, True)

dir = r'C:\Users\choll\AppData\Local\Programs\Python\Python39\Wartlog'
for file in os.scandir(dir):
    os.remove(file.path)
print("Cleared wartlog directory!")
os.chdir(r"C:\Users\choll\AppData\Local\Programs\Python\Python39\Wartlog")
cwd = os.getcwd()
print("Moved into", cwd)


now = datetime.now()
currenttime = now.strftime("%d-%m-%Y %I-%M.avi")
# display screen resolution, get it from your OS settings
SCREEN_SIZE = (2560, 1440)
# define the codec
fourcc = cv2.VideoWriter_fourcc(*"XVID")
# create the video write object
out = cv2.VideoWriter(currenttime, fourcc, 5.0, (SCREEN_SIZE))
print("Saving Video as ", currenttime)
firsttime = True
while True:
    # make a screenshot
    img = pyautogui.screenshot()
    # convert these pixels to a proper numpy array to work with OpenCV
    frame = np.array(img)
    # convert colors from BGR to RGB
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    # write the frame
    out.write(frame)
    # show the frame
    cv2.imshow("Video", frame)
    if firsttime == True:
        hwnd = win32gui.FindWindow(None, "Video")
        x0, y0, x1, y1 = win32gui.GetWindowRect(hwnd)
        w = x1 - x0 # width
        h = y1 - y0 # height

        win32gui.MoveWindow(hwnd, 2560, 1440, 50, 50, True)
        firsttime = False
    # if the user clicks q, it exits
    if cv2.waitKey(1) == ord("q"):
        break

# make sure everything is closed when exited
cv2.destroyAllWindows()
out.release()
