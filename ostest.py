import os
import random
import time
from pynput.keyboard import Key, Controller
keyboard = Controller()

time.sleep(2)

keyboard.press(Key.space)

time.sleep(0.1)

keyboard.release(Key.space)

time.sleep(0.05)

keyboard.press(Key.space)

time.sleep(0.1)

time.sleep(0.1)

keyboard.release(Key.space)
time.sleep(random.random() * 1 + .2)
keyboard.press(Key.space)

time.sleep(0.1)

keyboard.release(Key.space)

time.sleep(0.1)

keyboard.press(Key.space)

time.sleep(0.2)


keyboard.release(Key.space)