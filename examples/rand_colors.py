
'''
    LaunchPy Random Color Example

    This just demonstrates setting colors through LaunchPy
'''

from os import system
from launchpy import Launchpad, BindingHandler, LaunchpadMk2
import random
import time

# Creates a Launchpad Class for Mk2
lp = Launchpad(LaunchpadMk2)

# Adds an event to be called every tick
@lp.AddEvent
def colormod(lp, *a):
    for x in range(0, 9):
        for y in range(0, 9):
            lp.SetColor(x, y, random.randint(1, 100), mode="code")
            time.sleep(0.1)
    
    for y in range(0, 9):
        for x in range(0, 9):
            lp.SetColor(x, y, 0, mode="code")

        time.sleep(0.05)

# Starts the event loop
lp.MainLoop()