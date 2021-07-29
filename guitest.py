import win32gui

hwnd = win32gui.FindWindow(None, "Command Prompt - guitest.py")

x0, y0, x1, y1 = win32gui.GetWindowRect(hwnd)
w = x1 - x0 # width
h = y1 - y0 # height

win32gui.MoveWindow(hwnd, 1255, 680, 1315, 770, True)

