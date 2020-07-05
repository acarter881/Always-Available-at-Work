import pyautogui
import time

while True:
    time.sleep(10)
    for i in range(1,144,4):
        pyautogui.moveTo(960,i*4)
    pyautogui.press('shift')
    print('Shift was pressed at {}'.format(time.strftime('%I:%M:%S')))
