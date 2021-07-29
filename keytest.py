import keyboard
from pynput.keyboard import Key, Controller
kkeyboard = Controller()

kkeyboard.press("p")
keyboard.on_press_key("p", lambda _:print("You pressed p"))
