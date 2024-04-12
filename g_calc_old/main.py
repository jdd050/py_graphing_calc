# imports
import turtle as trtl
import os
from datetime import datetime, date
from func import *
from grid import *

# current time
now = datetime.now()
today = date.today()
currentTime = now.strftime("%H:%M:%S")
currentDate = today.strftime("%m/%d/%Y")

# start log
try: # open file
    cwd = os.getcwd()
    with open("log.txt", 'a') as instance:
        instance.write(f'== LOG OPEN SUCCESS, on {currentDate} @{currentTime} ==\n')
        pass
except OSError: # error handling
    print(f'OSError @ {cwd}, {currentTime}')
finally:
    pass

# method calls
cp.drawAxes(None)
cp.drawGrid(None)
func.debug(None)
func.doFunc(None)

# persist window
wn.mainloop()