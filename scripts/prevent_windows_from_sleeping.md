# Prevent Windows From Sleeping

This is useful if you are downloading a large file that is dependant on the session being active, or where you do not want your computer to sleep. Do not use in public places.

```python
from time import sleep
import pyautogui
import sys
import time
from datetime import datetime

def main():

        pyautogui.FAILSAFE = False
        sleep_time = None

        if ((len(sys.argv)<2) or (sys.argv[1].isalpha()) or (int(sys.argv[1])<1)): # check if the argument is a valid number else 3
            sleep_time = 1 # default
            print("Sleep time is: ", sleep_time)
        else:
            sleep_time = int(sys.argv[1])
            print("Sleep time is :", sleep_time)
        try:
            # an infinite loop. Play with the volume buttons, then reset and wait for the given sleep_time
            while (True):
                x = 0
                while (x<sleep_time):
                    time.sleep(50)
                    x += 1
                pyautogui.press('volumeup')
                time.sleep(1)
                pyautogui.press('volumedown')
                time.sleep(3)
                now = datetime.now().strftime("%H:%M:%S")
                print(f"Pressed some buttons at {now}.")
        except KeyboardInterrupt:
            print("Stopped")
            pass

if __name__ == '__main__':
    main()
```
