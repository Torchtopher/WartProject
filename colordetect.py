# Imports stuff
import win32gui
import numpy as np
import cv2
import random
from random import randint
from mss import mss
import pyautogui
import time
from pynput.keyboard import Key, Controller
from pynput.mouse import Button, Controller as MController
import random
import win32gui
# Sets the minecraft window to right size
hwnd = win32gui.FindWindow(None, 'Minecraft 1.8.9')

x0, y0, x1, y1 = win32gui.GetWindowRect(hwnd)
w = x1 - x0 # width
h = y1 - y0 # height

win32gui.MoveWindow(hwnd, -10, 0, 1280, 1450, True)


pythonpath = r"C:\Users\choll\AppData\Local\Programs\Python\Python39\python.exe"
try:
	hwnd = win32gui.FindWindow(None, pythonpath)
	
	x0, y0, x1, y1 = win32gui.GetWindowRect(hwnd)
	w = x1 - x0 # width
	h = y1 - y0 # height
	
	win32gui.MoveWindow(hwnd, 1255, 960, 1315, 490, True)
	#BGR NOT RGB 
except:
	hwnd = win32gui.FindWindow(None, "Command Prompt - colordetect.py")
	
	x0, y0, x1, y1 = win32gui.GetWindowRect(hwnd)
	w = x1 - x0 # width
	h = y1 - y0 # height
	
	win32gui.MoveWindow(hwnd, 1255, 960, 1315, 490, True)
#Moves mouse to the "Back to game" button and clicks it 
time.sleep(7)


# Start a while loop
#'top': 30, 'left': 0, 'width': 1280, 'height': 1400
time.sleep(1)
jumpcooldown = 0
while(1):
	red = 0
	blue = 0 
	green = 0
	jump = False
	# Takes screenshot every loop around the cursor
	img = pyautogui.screenshot(region=(435,300, 435, 900))
	img = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)
	# writes image first becuase it only worked like that lol 
	cv2.imwrite("pyautoguiss.png", img)

	# Then reads it and does the color detection
	imageFrame = cv2.imread("pyautoguiss.png")

	# THIS PART WAS COPIED IDK WHAT GOES ON BUT I MADE IT WORK
	# Reading the video from the
	# webcam in image frames



	# Convert the imageFrame in
	# BGR(RGB color space) to
	# HSV(hue-saturation-value)
	# color space
	hsvFrame = cv2.cvtColor(imageFrame, cv2.COLOR_BGR2HSV)
	#BGR NOT RGB 
	# Set range for red color and
	# define mask
	red_lower = np.array([0, 50, 50], np.uint8)
	red_upper = np.array([10, 255, 255], np.uint8)
	red_mask = cv2.inRange(hsvFrame, red_lower, red_upper)
	#BGR NOT RGB 
	# Set range for green color and
	# define mask
	green_lower = np.array([25, 52, 72], np.uint8)
	green_upper = np.array([102, 255, 255], np.uint8)
	green_mask = cv2.inRange(hsvFrame, green_lower, green_upper)
	#BGR NOT RGB 
	# Set range for blue color and
	# define mask
	blue_lower = np.array([94, 80, 2], np.uint8)
	blue_upper = np.array([120, 255, 255], np.uint8)
	blue_mask = cv2.inRange(hsvFrame, blue_lower, blue_upper)
	
	# Morphological Transform, Dilation
	# for each color and bitwise_and operator
	# between imageFrame and mask determines
	# to detect only that particular color
	kernal = np.ones((5, 5), "uint8")
	
	# For red color
	red_mask = cv2.dilate(red_mask, kernal)
	res_red = cv2.bitwise_and(imageFrame, imageFrame,
							mask = red_mask)
	
	# For green color
	green_mask = cv2.dilate(green_mask, kernal)
	res_green = cv2.bitwise_and(imageFrame, imageFrame,
								mask = green_mask)
	
	# For blue color
	blue_mask = cv2.dilate(blue_mask, kernal)
	res_blue = cv2.bitwise_and(imageFrame, imageFrame,
							mask = blue_mask)


	# Creating contour to track blue color
	contours, hierarchy = cv2.findContours(blue_mask,
										cv2.RETR_TREE,
										cv2.CHAIN_APPROX_SIMPLE)
	for pic, contour in enumerate(contours):
		area = cv2.contourArea(contour)
		if(area > 300):
			x, y, w, h = cv2.boundingRect(contour)
			imageFrame = cv2.rectangle(imageFrame, (x, y),
									(x + w, y + h),
									(255, 0, 0), 2)
			blue = blue + 1
			# tracks blue objects and if seen writes to a file that wartmacro looks at
			if blue > 0:
				f = open("wartconf.txt", "r+")
				filedata = f.read()
				# Makes sure nothing else is written
				if filedata == "":
					f.write("BLUE")
					print("BLUE written to wartconf")
				else: 
					print("File already has " + str(filedata) + " in it")
				f.close()

			cv2.putText(imageFrame, "Blue Colour", (x, y),
						cv2.FONT_HERSHEY_SIMPLEX,
						1.0, (255, 0, 0))

	# Creating contour to track red color
	contours, hierarchy = cv2.findContours(red_mask,
										cv2.RETR_TREE,
										cv2.CHAIN_APPROX_SIMPLE)
	#BGR NOT RGB 	
	for pic, contour in enumerate(contours):
		area = cv2.contourArea(contour)
		if(area > 1000):
			# Tracks red objects and if seen jumps
			red = red + 1

			if jump == False and jumpcooldown == 0 and blue == 0:

				keyboard = Controller()
				print("Jumping!!")

				
				
				keyboard.press(Key.space)
				
				time.sleep(0.1)
				
				keyboard.release(Key.space)
				
				time.sleep(0.05)
				
				keyboard.press(Key.space)
				
				time.sleep(0.1)
				
				time.sleep(0.1)
				
				keyboard.release(Key.space)
				time.sleep(random.random() * 3 + .2)
				keyboard.press(Key.space)
				
				time.sleep(0.1)
				
				keyboard.release(Key.space)
				
				time.sleep(0.1)
				
				keyboard.press(Key.space)
				
				time.sleep(0.1)
				
				
				keyboard.release(Key.space)
				jump = True
				jumpcooldown = 5
			

			x, y, w, h = cv2.boundingRect(contour)
			imageFrame = cv2.rectangle(imageFrame, (x, y),
									(x + w, y + h),
									(0, 0, 255), 2)
			
			cv2.putText(imageFrame, "Red Colour", (x, y),
						cv2.FONT_HERSHEY_SIMPLEX, 1.0,
						(0, 0, 255))	

	# Creating contour to track green color
	contours, hierarchy = cv2.findContours(green_mask,
										cv2.RETR_TREE,
										cv2.CHAIN_APPROX_SIMPLE)
		#BGR NOT RGB 
	for pic, contour in enumerate(contours):
		area = cv2.contourArea(contour)
		if(area > 300):
			x, y, w, h = cv2.boundingRect(contour)
			imageFrame = cv2.rectangle(imageFrame, (x, y),
									(x + w, y + h),
									(0, 255, 0), 2)
			green = green + 1
			
			cv2.putText(imageFrame, "Green Colour", (x, y),
						cv2.FONT_HERSHEY_SIMPLEX,
						1.0, (0, 255, 0))

			
	# Tells how many of each color objects there are
	print(str(red) + " red, " + str(green) + " green, " + str(blue) + " blue")
	# Makes it so you can only jump every 50 seconds about 
	if jumpcooldown > 0:
		jumpcooldown = jumpcooldown - .01
		jumpcooldown = round(jumpcooldown, 2)
		if jumpcooldown == int(jumpcooldown):
			print("Jumpcooldown is " + str(jumpcooldown))
	# Program Termination
	cv2.imshow("Multiple Color Detection in Real-TIme", imageFrame)
	if cv2.waitKey(10) & 0xFF == ord('q'):
		cap.release()
		cv2.destroyAllWindows()
		break
