
#Normal importing of libraries
import random
from random import randint
import time
from pynput.keyboard import Key, Controller
from pynput.mouse import Button, Controller as MController
import os
import sys
import win32gui
global apress
global dpress
from datetime import datetime

# Sets controllers for pynput mouse and keyboard
keyboard = Controller()
mouse = MController()

hwnd = win32gui.FindWindow(None, 'Command Prompt - wartmacro.py')

x0, y0, x1, y1 = win32gui.GetWindowRect(hwnd)
w = x1 - x0 # width
h = y1 - y0 # height

win32gui.MoveWindow(hwnd, 1255, -5, 1315, 490, True)

# Starts color detector program
directory = r"C:\Users\choll\AppData\Local\Programs\Python\Python39\WartProject"
os.chdir(directory)
colordetctpath = r"C:\Users\choll\AppData\Local\Programs\Python\Python39\WartProject\colordetect.py"
wartloggerpath = r"C:\Users\choll\AppData\Local\Programs\Python\Python39\WartProject\wartlogger.py"
corddetectpath = r"C:\Users\choll\AppData\Local\Programs\Python\Python39\WartProject\corddetect.py"

os.startfile(wartloggerpath)

time.sleep(.5)
os.startfile(colordetctpath)

time.sleep(2)
os.startfile(corddetectpath)

time.sleep(4)
#Sets variables at the start
atime = False
watertime = False
spawntime = False
apress = False
dpress = False
cooldowntime = False


f = open("wartconf.txt", "r+")
f.seek(0)
f.write("")
f.truncate(0)
f.close()

f = open("dirconf.txt", "r+")
f.seek(0)
f.write("")
f.truncate(0)
f.close()

def wartconfcheck():

	f = open("wartconf.txt", "r+")
	filedata = f.read()
	# Looks for blue
	if filedata == "BLUE":
		print("Blue seen! Going back to island.")
		#Releases all possible keys that could be pressed, does nothing if they are not pressed
		mouse.release(Button.left)
		keyboard.release("a")
		keyboard.release("d")
		# Uses random delays and loops to make the typing of /is look natural
		for char in "/is":
			keyboard.press(char)
			keyboard.release(char)
			time.sleep(random.random() / 4)
		keyboard.press(Key.enter)
		keyboard.release(Key.enter)
		# Waits some time to make sure you get back to your island
		time.sleep(randint(3,5))
		for x in range(65):
			mouse.move(0, -2)
			time.sleep(0.001)
		# Erases file
		f.seek(0)
		f.write("")
		f.truncate(0)
		# Uses your last known direction to set you back up farming
		startfarming()
		f.close()
		time.sleep(randint(1,3))
		# Sets A to 0 so no random actions can be taken
		a = 0

def dirconfcheck():
	f = open("dirconf.txt", "r+")
	filedata = f.read()
	# Looks for blue
	if filedata == "SWITCH":
		print("Switching directions!")
		#Releases all possible keys that could be pressed, does nothing if they are not pressed
		mouse.release(Button.left)
		keyboard.release("a")
		keyboard.release("d")

		# Erases file
		f.seek(0)
		f.write("")
		f.truncate(0)
		f.close()
		# Uses your last known direction to set you back up farming
		switch()

		# Sets A to 0 so no random actions can be taken
		a = 0
def switch():
	global apress
	global dpress
	if apress == True and dpress == False:
		mouse.press(Button.left)
		keyboard.release("a")
		time.sleep(random.random() / 6)
		keyboard.press("d")
		dpress = True
		apress = False
		time.sleep(2)
		return

	if dpress == True and apress == False:
		mouse.press(Button.left)
		keyboard.release("d")
		time.sleep(random.random() / 6)
		keyboard.press("a")
		apress = True
		dpress = False
		time.sleep(2)
		return
def startfarming():
	global apress
	global dpress
	if apress == True:
		mouse.press(Button.left)
		keyboard.press("a")

	if dpress == True:
		mouse.press(Button.left)
		keyboard.press("d")

# Random actions to preform while moving
# Also checks for inputs from the color detetor script
def randomhandler():
	global a
	global waterbreak
	global spawnseed

	global spawntime
	global atime
	global watertime
	global spawnstarttime
	global astarttime
	global waterstarttime
	global cooldowntime
	global cooldowntimer
	if cooldowntime == False:
		cooldowntimer = time.time()
		cooldowntime = True
	if spawntime == False:
		spawnseed = randint(240, 480)
		spawnstarttime = time.time()
		spawntime = True

	if atime == False:
		a = randint(20, 70)
		atime = True
		astarttime = time.time()
	if watertime == False:
		waterbreak = randint(3000, 4000)
		watertime = True
		waterstarttime = time.time()
	if time.time() - spawnstarttime >= spawnseed:
		print("Setting Spawn!")
		spawnstarttime = time.time()
		mouse.release(Button.left)
		for char in "/setspawn":
			keyboard.press(char)
			keyboard.release(char)
			time.sleep(random.random() / 4)
		keyboard.press(Key.enter)
		keyboard.release(Key.enter)

		spawnseed = randint(240,480)
		print("spawnseed is " + str(spawnseed))
		mouse.press(Button.left)



	if time.time() - astarttime >= a:
		atime = False
		print(str(a) + " Seconds elapsed, prefoming random action")

		b = randint(0,1)
		# Tells you
		print("Random Seed is " + str(b))

		# Random actions that could be chosen
		if b == 0:
			keyboard.press(Key.shift)
			time.sleep(0.05)
			keyboard.release(Key.shift)
			time.sleep(random.random())
			keyboard.press(Key.shift)
			time.sleep(0.07)
			keyboard.release(Key.shift)

		elif b == 1:
			keyboard.press("w")
			time.sleep(0.05)
			keyboard.release("w")
			time.sleep(random.random())
			keyboard.press("s")
			time.sleep(random.random())
			keyboard.release("s")
	if time.time() - waterstarttime >= waterbreak:
		watertime = False
		print(str(waterbreak) + " Seconds elapsed, taking water break! :)")

		mouse.release(Button.left)
		keyboard.release("a")
		keyboard.release("d")
		watertime = randint(120, 360)
		print("Takeing a " + str(watertime) + " second break!")
		time.sleep(watertime)
		startfarming()
	if time.time() - cooldowntimer >= 1:
		spawntimeleft = int(spawnseed - (time.time() - spawnstarttime))
		watertimeleft = int(waterbreak - (time.time() - waterstarttime))
		atimeleft = int(a - (time.time() - astarttime))
		print(str(watertimeleft) + " seconds left until waterbreak")
		print(str(spawntimeleft) + " seconds left until setting spawn")
		print(str(atimeleft) + " seconds left until a random action")
		cooldowntime = False



		#elif b == 2:
		#	startpos = mouse.position()
		#	print(startpos)
		#	c = randint(-3, 3)
		#	d = randint(-3, 3)
		#
		#	for x in range(10)
		#		mouse.move(randint(c, d))
		#		time.sleep(0.01)
		#	time.sleep(randint(1,3))

		#	for x in range(10)
		#		mouse.move(randint(-c, -d))
		#		time.sleep(0.01)



def randomactions():

	global spawnseed
	# Uses self made timer
	while True:
		# Random number to decide when random actions will happen



		randomhandler()
		dirconfcheck()
		# Opens file used by the color detector to check for what to do
		wartconfcheck()







# The loop that starts farming keeps track of which way you were going with apress and dpress
firstrun = True
while True:
	if firstrun == True:
		mouse.press(Button.left)
		keyboard.press("a")
		apress = True

		firstrun = False

	randomactions()
