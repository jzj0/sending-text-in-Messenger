import pyautogui
import time
message=3000
while message>0:
    time.sleep(1)
    pyautogui.typewrite("Hello")
    time.sleep(1)
    pyautogui.press('enter')
    message=message-1
