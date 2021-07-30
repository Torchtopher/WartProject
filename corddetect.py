from PIL import Image as im
import pytesseract
import cv2
import pyautogui
import numpy as np
import time
import win32gui
from pynput.mouse import Button, Controller as MController

pytesseract.pytesseract.tesseract_cmd = "C:\\Users\\choll\\AppData\\Local\\Programs\\Tesseract-OCR\\tesseract.exe"
firstloop = True
cooldown = 0

pythonpath = r"C:\Users\choll\AppData\Local\Programs\Python\Python39\python.exe"
try:
    hwnd = win32gui.FindWindow(None, pythonpath)

    x0, y0, x1, y1 = win32gui.GetWindowRect(hwnd)
    w = x1 - x0 # width
    h = y1 - y0 # height

    win32gui.MoveWindow(hwnd, 1255, 480, 1315, 495, True)
    #BGR NOT RGB
except:
    hwnd = win32gui.FindWindow(None, "Command Prompt - corddetect.py")

    x0, y0, x1, y1 = win32gui.GetWindowRect(hwnd)
    w = x1 - x0 # width
    h = y1 - y0 # height

    win32gui.MoveWindow(hwnd, 1255, 500, 1315, 480, True)

hwnd = win32gui.FindWindow(None, "Task Manager")

x0, y0, x1, y1 = win32gui.GetWindowRect(hwnd)
w = x1 - x0 # width
h = y1 - y0 # height

win32gui.MoveWindow(hwnd, 1255, 480, 1315, 495, True)

mouse = MController()

mouse.position = (635, 435)
mouse.press(Button.left)
mouse.release(Button.left)
time.sleep(.5)
while True:


    img = pyautogui.screenshot(region=(65,212, 460, 41))
    img = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)
    cv2.imwrite("cords.png", img)
    image = im.open(r'cords.png')

    image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2HSV)
    hsv_image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2HSV)
    color_lower = np.array([100, 255, 220])
    color_upper = np.array([200, 255, 230])
    mask = cv2.inRange(hsv_image, color_lower, color_upper)
    result = cv2.bitwise_and(image, image, mask=mask)
    image = cv2.cvtColor(np.array(result), cv2.COLOR_RGB2GRAY)
    image = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
    cv2.imwrite("cords.png", image)
    text = pytesseract.image_to_string(image, lang='mc')
    split_string = text.split("X ", 1)
    try:
        text = split_string[1]
    except:
        text = split_string[0]
    split_string = text.split("X ", 1)
    try:
        text = split_string[0]
    except:
        text = split_string[1]

    print(text)
    if firstloop == True:
        ycord = text
        firstloop = False
    if firstloop != True:
        oldycord = ycord
        ycord = text

        if oldycord != ycord and cooldown <= 0:
            print("You have moved!")
            f = open("dirconf.txt", "r+")
            f.write("SWITCH")
            f.close()
            print("dirconf updated")
            cooldown = 2

    if cooldown > 0:
        cooldown = cooldown - .05
        cooldown = round(cooldown, 2)
        if cooldown == int(cooldown):
            print("Cooldown is " + str(cooldown))
    cv2.imshow("Cord Detection", image)

    hwnd = win32gui.FindWindow(None, "Cord Detection")

    x0, y0, x1, y1 = win32gui.GetWindowRect(hwnd)
    w = x1 - x0 # width
    h = y1 - y0 # height

    win32gui.MoveWindow(hwnd, 2000, 800, w, h, True)

    if cv2.waitKey(10) & 0xFF == ord('q'):
        cap.release()
        cv2.destroyAllWindows()
        break
