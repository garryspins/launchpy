
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"

from launchpy.bindings import BindingHandler
from launchpad_py import *

# Constant Types
types = {
    LaunchpadPro        : ["Pro",       None],
    LaunchpadProMk3     : ["ProMk3",    None],
    LaunchpadMiniMk3    : ["Pro",       "minimk3"],
    LaunchpadLPX        : ["Pro",       "lpx"],
    LaunchpadMk2        : ["Mk2",       "mk2"],
    LaunchControlXL     : ["XL",        "control xl"],
    LaunchKeyMini       : ["LKM",       "launchkey"],
    Dicer               : ["Dcr",       "dicer"],
    MidiFighter64       : ["MF64",      None],
    Launchpad           : ["Mk1",       None],
#   Type                : [mode,        opentype]
}

class LaunchpadFailed(Exception):
    def __init__(*a):
        pass

class Launchpad:
    events = []

    # Base Class Methods
    def __init__(self, cls, silent=False, autoopen=True, doanim=False):
        self.launch = cls()
        self.cls = cls
        self.info = self.GetInfo(cls)
        self.type = self.info[0]

        if autoopen:
            if self.launch.Check(0):
                try:
                    self.launch.Open(0, self.info[1])
                except AttributeError:
                    print("Please Reinstall launchpy!")
                self.ButtonFlush()
            else:
                raise LaunchpadFailed("Failed to Recognize Launchpad Of Basetype " + type(self.launch).__name__)

            print("Recognized Launchpad Of Basetype " + type(self.launch).__name__)

        # if autoopen and doanim:
            # self.Animation()
            # pass

    # def Animation(self):
    #     if not self.type == "Mk2": return # Needs to support other pads, idk sizes rn
    #     from time import sleep

    #     curposout = 0
    #     curposin = 0
    #     color = 1
    #     while 1:
    #         self.SetColor(curposin, curposout, color, color, b=color)
    #         self.SetColor(curposout, curposin, color, color, b=color)

    #         self.SetColor(curposin - 1, curposout - 1, 0, 0)
    #         self.SetColor(curposout - 1, curposin - 1, 0, 0)

    #         curposout = curposout + 1

    #         if curposout >= 10:
    #             color = color + 2
    #             curposin = curposin + 1
    #             curposout = curposin

    #         if curposin >= 10:
    #             break

    #         sleep(0.1)

    #     self.Clear()


    # Events
    def MainLoop(self):
        while 1:
            buttons = self.ButtonState()
            for x in self.events:
                x[0](self, buttons, x[1])

    def AddEvent(self, f, args=()):
        self.events.append([f, args])


    # Gay SubMethods
    @staticmethod
    def GetInfo(type):
        return types.get(type)

    def Close(self):
        return self.launch.Close()

    def Reset(self):
        return self.launch.Reset()

    def ButtonFlush(self):
        return self.launch.ButtonFlush()

    def Clear(self):
        self.Reset()
        self.ButtonFlush()

    def ListAll(self, search=""):
        return self.launch.ListAll(search)

    def EventRaw(self):
        return self.launch.EventRaw()

    def IsMk2Compat(self):
        return (self.type == "Mk2") or (self.type == "Pro") or (self.type == "ProMk3")

    # Cancer Compat Functions, Thanks Launchpad.py!
    def GetColor(self, red, green):
        if (self.type == "Mk1") or (self.type == "XL"):
            return self.launch.LedGetColor(red, green)
        
    def SetColor(self, x, y, r, g=0, b=None, mode=""):
        if (self.type == "Mk1"):
            return self.launch.LedCtrlXY(x, y, r, g)
        elif self.IsMk2Compat():
            if mode == "code":
                return self.launch.LedCtrlXYByCode(x, y, r)
            elif mode == "rgb":
                return self.launch.LedCtrlXYByRGB(x, y, r)            
            else:
                return self.launch.LedCtrlXY(x, y, r, g, b)

    def ButtonState(self):
        return self.launch.ButtonStateXY()