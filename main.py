import pyautogui # This Python library is required in order to run this code; If you don't have this 3rd party module installed, Google it and install prior to running this code.
import time      # This is a standard Python library, used in this example to delay the time between each press of the "shift" key.

pyautogui.FAILSAFE = False # This to ensure the script doesn't fail when you have the mouse pointer in the top left corner.

while 1: # I use "1" instead of "True" to shorten the code by three characters.
    time.sleep(250) # This is set to 250 seconds
    """
    You can use the code below, but it isn't necessary. After testing, I've found that moving the mouse is a nuisance if you're using the computer. 
    It turns out that the call to "shift" is all that's necessary to keep the computer awake (i.e., prevent a log out of Windows).

    for i in range(1,144,4):
        pyautogui.moveTo(960,i*4)
    """
    pyautogui.press('shift') # I found that the "shift" key is a very good key to press - I never notice any disruption when running this script while doing my day to day work.
    print('Shift was pressed at {}'.format(time.strftime('%I:%M:%S'))) # This is solely for informational purposes; this line prints the time at which "shift" is pressed to the console.
