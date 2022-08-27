import pyautogui 
import time   

# Ensures the script doesn't fail when you have the mouse pointer in the top left corner
pyautogui.FAILSAFE = False  

# The `shift` key is a good key to press, but a different key may be selected (see https://pyautogui.readthedocs.io/en/latest/keyboard.html)
key = 'volumemute'

# Number of press repetitions
presses = 1

# Infinite loop
while 1:
    time.sleep(3)
    # Press the `key`
    pyautogui.press(keys=key, presses=presses)