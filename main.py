import pyautogui 
import time
import webbrowser  
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtCore import *
from typing import Tuple

pyautogui.FAILSAFE = False

KEY_OPTIONS = ['\t', '\n', '\r', ' ', '!', '"', '#', '$', '%', '&', "'", '(',
')', '*', '+', ',', '-', '.', '/', '0', '1', '2', '3', '4', '5', '6', '7',
'8', '9', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`',
'a', 'b', 'c', 'd', 'e','f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '{', '|', '}', '~',
'accept', 'add', 'alt', 'altleft', 'altright', 'apps', 'backspace',
'browserback', 'browserfavorites', 'browserforward', 'browserhome',
'browserrefresh', 'browsersearch', 'browserstop', 'capslock', 'clear',
'convert', 'ctrl', 'ctrlleft', 'ctrlright', 'decimal', 'del', 'delete',
'divide', 'down', 'end', 'enter', 'esc', 'escape', 'execute', 'f1', 'f10',
'f11', 'f12', 'f13', 'f14', 'f15', 'f16', 'f17', 'f18', 'f19', 'f2', 'f20',
'f21', 'f22', 'f23', 'f24', 'f3', 'f4', 'f5', 'f6', 'f7', 'f8', 'f9',
'final', 'fn', 'hanguel', 'hangul', 'hanja', 'help', 'home', 'insert', 'junja',
'kana', 'kanji', 'launchapp1', 'launchapp2', 'launchmail',
'launchmediaselect', 'left', 'modechange', 'multiply', 'nexttrack',
'nonconvert', 'num0', 'num1', 'num2', 'num3', 'num4', 'num5', 'num6',
'num7', 'num8', 'num9', 'numlock', 'pagedown', 'pageup', 'pause', 'pgdn',
'pgup', 'playpause', 'prevtrack', 'print', 'printscreen', 'prntscrn',
'prtsc', 'prtscr', 'return', 'right', 'scrolllock', 'select', 'separator',
'shift', 'shiftleft', 'shiftright', 'sleep', 'space', 'stop', 'subtract', 'tab',
'up', 'volumedown', 'volumemute', 'volumeup', 'win', 'winleft', 'winright', 'yen',
'command', 'option', 'optionleft', 'optionright']

def gather_options() -> Tuple[str, int, int]:
    global key, interval, presses

    with open(file='./config.txt', mode='r') as f:
        data = f.readlines()

    key = data[0].split('[INSERT VALUE TO THE RIGHT]')[-1].strip()
    interval = data[1].split('[INSERT VALUE TO THE RIGHT]')[-1].strip()

    if key in KEY_OPTIONS:
        pass
    else:
        key = 'shift'

    if interval.isnumeric():
        if int(interval) > 0:
            interval = int(interval)
    else:
        interval = 250

    presses = 1

    return key, interval, presses

class MyGUI(QMainWindow):
    def __init__(self) -> None:
        super(MyGUI, self).__init__()
        uic.loadUi('./ui/never away.ui', self)

        self.show()

        self.action_Exit.triggered.connect(qApp.quit)
        self.action_About.triggered.connect(lambda: webbrowser.open('https://github.com/acarter881/Always-Available-at-Work'))

        self.press_count = 0
        self.label.setText(f'Key selected: {key}')
        self.label_2.setText(f'Interval selected: {interval} seconds')

        self.worker = WorkerThread()
        self.worker.start()
        self.worker.update_progress.connect(self.evt_update_progress)

    def evt_update_progress(self, val) -> None:
        self.textBrowser.append(val)
        self.press_count += 1
        self.label_3.setText(f'Number of presses in this session: {self.press_count}')

class WorkerThread(QThread):
    update_progress = pyqtSignal(str)

    def run(self) -> None:
        while 1:
            time.sleep(interval)
            pyautogui.press(keys=key, presses=presses)
            self.update_progress.emit(f"{key.title()} was pressed at {time.strftime('%I:%M:%S %p')}")

def main() -> None:
    app = QApplication([])
    window = MyGUI()
    app.exec_()

# Call the function
if __name__ == '__main__':
    gather_options()
    main()