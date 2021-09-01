
'''
    LaunchPy Binding Tests
'''

from launchpy import Launchpad, BindingHandler, LaunchpadMk2

lp = Launchpad(LaunchpadMk2)
binder = BindingHandler(lp)

@binder.Binding(0, 1)
def oke(lp, *a):
    print("yea ok mhm sure")

@binder.Binding(0, 2)
def butthole(lp, *a):
    print("poop")

@binder.Mk2Volume()
def gay(*a):
    print(123)

@binder.Mk2RecordArm()
def yea(*a):
    print("yea")

lp.MainLoop()