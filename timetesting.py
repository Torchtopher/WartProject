import time
from random import randint
spawntime = False
while True:
	if spawntime == False:
		spawnseed = randint(5, 10)
		spawnstarttime = time.time()
		spawntime = True
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
	timeleft = int(spawnseed - (time.time() - spawnstarttime))
	print(str(timeleft) + " seconds left!")
