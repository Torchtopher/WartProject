from PIL import Image as im
import pytesseract
import cv2
import pyautogui
import numpy as np
import time
time.sleep(2)
pytesseract.pytesseract.tesseract_cmd = "C:\\Users\\choll\\AppData\\Local\\Programs\\Tesseract-OCR\\tesseract.exe"
img = pyautogui.screenshot(region=(218,212, 160, 40))
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
print(text)