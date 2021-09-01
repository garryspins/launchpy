
'''
    Orion (me, the guy that made it)'s Epic Bindings 

    Thisll only work with a Mk2, since thats what i have
'''

from launchpy import Launchpad, BindingHandler, LaunchpadMk2
import keyboard

lp = Launchpad(LaunchpadMk2)
bind = BindingHandler(lp)

@bind.Mk2Up(color={"r": 1, "g": 50, "b": 1})
def volup(*a):
    keyboard.press("volume up")
    keyboard.release("volume up")

@bind.Mk2Down(color={"r": 50, "g": 1, "b": 1})
def voldown(*a):
    keyboard.press("volume down")
    keyboard.release("volume down")

@bind.Mk2Left(color={"r": 1, "g": 25, "b": 25})
def nexttrk(*a):
    keyboard.press("next track")
    keyboard.release("next track")


@bind.Mk2Right(color={"r": 1, "g": 25, "b": 25})
def prevtrk(*a):
    keyboard.press("previous track")
    keyboard.release("previous track")

lp.MainLoop()