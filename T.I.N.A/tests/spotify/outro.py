import pyautogui
import os
import time

os.system("spotify")
time.sleep(5)
pyautogui.write("Neopolitan Dreams", interval = 0.1)

for key in ['enter', 'pagedown', 'tab', 'enter', 'enter']:
    time.sleep(2)
    pyautogui.press(key)



