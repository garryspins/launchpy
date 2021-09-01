
'''
    LaunchPy Binding Examples

    This shows how to add Bindings to a Launchpad

    Required Packages:
        keyboard
'''

from os import system
from launchpy import Launchpad, BindingHandler, LaunchpadMk2
import keyboard

# Creates a Launchpad Class for the Mk2
lp = Launchpad(LaunchpadMk2)

# Adds a Binding Handler to that launchpad
binder = BindingHandler(lp)

# Adds a function to be called when you release the button 0,1 (very top left)
# This just writes out some text
@binder.Binding(0, 1)
def write_something(lp, *a):
    keyboard.write("LaunchPy is honestly kinda cute")

# Adds a function to be called when you press the button 0,2
# Stops the program
@binder.Binding(0, 2)
def stop(lp, *a):
    exit()

# Starts the event loop
# This just handles events internally
lp.MainLoop()