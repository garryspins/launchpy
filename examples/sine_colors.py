
'''
    LaunchPy Sine Example

    This just demonstrates setting colors through LaunchPy
'''

from os import system
from launchpy import Launchpad, BindingHandler, LaunchpadMk2
import time
import math

# Creates a Launchpad Class for Mk2
lp = Launchpad(LaunchpadMk2)

# Adds an event to be called every tick
wrap = 1
@lp.AddEvent
def spiral(lp, *a):
    global wrap
    for x in range(0, 9):
        sin = math.floor(math.sin(round(time.time() * 1000) / 2) * 4) + 5
        for y in range(0, 9):
            lp.SetColor(x, sin, wrap, mode="code")
        time.sleep(0.5)
    wrap = wrap + 5

# Starts the event loop
lp.MainLoop()