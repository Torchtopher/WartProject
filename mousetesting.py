from pynput.mouse import Button, Controller as MController
import time
import random
from random import randint
import cv2
import keyboard
mouse = MController()
time.sleep(2)
for x in range(65):
	mouse.move(0, -2)
	time.sleep(0.001)

time.sleep(20)


startpos = mouse.position 
print(startpos)
print(type(startpos))
startpos = list(startpos)
for x in range(20):
	mouse.move(randint(-2, 3), randint(-3, 3))
	time.sleep(0.05)
x = startpos[0]
y = startpos[1]
xdif = mouse.position[0] - x
ydif = mouse.position[1] - y
xdif = -xdif
ydif = -ydif
for x in range(6):

	mouse.move(xdif / 6, ydif / 6)
	time.sleep(.05)

print("Here!")

time.sleep(3)
mouse.position = (startpos[0], startpos[1])
move = 0
time.sleep(2)
center = 1
def xycalc():


	xdif = mouse.position[0] - x
	ydif = mouse.position[1] - y
	xdif = -xdif
	ydif = -ydif

while True:
	if keyboard.is_pressed('q'):
		print("Quitting!")
		break
	bound = 20
	xmax = startpos[0] + bound
	xmin = startpos[0] - bound
	ymin = startpos[1] - bound
	ymax = startpos[1] + bound	
				


	x = random.randint(xmin, xmax)
	y = random.randint(ymin, ymax)
	xdif = mouse.position[0] - x
	ydif = mouse.position[1] - y
	print(x, y)
	xdif = -xdif
	ydif = -ydif
	print(xdif, ydif)
	if move == 10:
		move = 0
		x = startpos[0]
		y = startpos[1]
		xdif = mouse.position[0] - x
		ydif = mouse.position[1] - y
		xdif = -xdif
		ydif = -ydif
		print("Moving to center")
		center = 0

	for i in range(5):
		mouse.move(xdif / 5, ydif / 5)
		time.sleep(.0001)

	if center == 0:
		center = 1 
		print("In the center?")
		time.sleep(2)
	move = move + 1
	#mouse.position = (x, y)
		


upleftbound = [startpos[0] + 50, startpos[1] - 50]
print(upleftbound)
print(type(upleftbound))
time.sleep(1)
print(upleftbound[0])
print(upleftbound[1])




#for x in range(50):
#	mouse.move(1, 0)
#	time.sleep(0.00001)
center = True
left = False # 1
right = False # 2
up = False # 3
down = False # 4
upright = False # 5
upleft = False # 6
downright = False # 7
downleft = False # 8

direction = randint(1,8)
time.sleep(2)
#while True:
#	a = randint(5, 50)
#	b = round(random.uniform(-1, 1), 3)
#	c = round(random.uniform(-1, 1), 3)
#	print(a, b, c)
#	print("B is "  + str(b) + " C is " + str(c))
#	for x in range(a):
#		mouse.move(b, c)
#		time.sleep(0.0001)
#		#b = b / round(random.uniform(1, 1.1), 3)		
#		print(b)
#		#c = c / round(random.uniform(1, 2), 3)
#		print(c)
#