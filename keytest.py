import time
from pynput.keyboard import Key, Controller
import random
keyboard = Controller()
time.sleep(2)
while True:
    print("Jumping!!")
    keyboard.press(Key.space)
    time.sleep(0.1)
    keyboard.release(Key.space)
    time.sleep(0.05)
    keyboard.press(Key.space)
    time.sleep(0.1)
    time.sleep(0.1)
    keyboard.release(Key.space)
    jumpdelay = random.random() * 3 + .2
    print("jumpdelay is " + str(jumpdelay))
    time.sleep(jumpdelay)
    keyboard.press(Key.space)
    time.sleep(0.1)
    keyboard.release(Key.space)
    time.sleep(0.1)
    keyboard.press(Key.space)
    time.sleep(0.1)
    keyboard.release(Key.space)
