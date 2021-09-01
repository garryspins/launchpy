# LaunchPy - The Best Launchpad Library

LaunchPy is a library for controlling [Novation Launchpads](https://novationmusic.com/en/launch) through Python in a simple, dynamic way  
Launchpad at its core is a wrapper for [launchpad.py](https://github.com/FMMT666/launchpad.py), but LaunchPy provides much more, see below

## Features

- Builtin Event Handling
- Easy interfacing with [launchpad.py](https://github.com/FMMT666/launchpad.py)
- [Cross-Device Compatibility](#cross-device-compatibility)
- Binding Handlers, to make life easier
- Simple, Pythonic API using attributes

## API

The API is subject to change, and will be documented better later

`class Launchpad(class launchpad_type)` - Launchpad is the central class of the library, it takes a type from Launchpad.py
- `fn MainLoop()` - Runs the main event loop of the Launchpad, aka every event
- `fn AddEvent(fn func, tuple args)` - Adds an event to the event loop, can be used as an attribute
- `fn GetInfo(class launchpad_type) -> list` - Gets the information of the launchpad type given
- `fn Close() -> ?` - Closes the launchpad
- `fn Reset() -> ?` - Resets the launchpad
- `fn ButtonFlush()` - Flushes the launchpads buttons
- `fn Clear()` - Resets and Flushes
- `fn EventRaw() -> ?` - Returns the current raw event
- `fn IsMk2Compat() -> bool` - Returns if the launchpad is Mk2 function compatable
- `fn GetColor(red, green) -> ?` - Returns the color of the red green combo
- `fn SetColor(x, y, r, g=0, b=None, mode=None) -> ?` - Sets the color of the x,y given 
- `fn ButtonState() -> list` - Returns the current button state based on x, y  

`class BindingHandler(Launchpad lp)` (All methods should be used as attributes)
- `fn Binding(x, y, silent=False, method="release", color=False) -> BindingHandler.__internal__Binding` - Adds a binding to the x,y given, if silent is True then it wont output a message confirming it was added
- All the following methods are attributes that are helpers to the outside buttons on a Mk2, same args as Binding without x,y 
- - Mk2Up
- - Mk2Down
- - Mk2Left
- - Mk2Right
- - Mk2Session
- - Mk2User1
- - Mk2User2
- - Mk2Mixer
- - Mk2Volume
- - Mk2Pan
- - Mk2SendA
- - Mk2SendB
- - Mk2Stop
- - Mk2Mute
- - Mk2Solo
- - Mk2RecordArm


## Cross-Device Compatibility
The only device tested is the Mk2, thats why the library is mainly focused on supporting it  
**PLEASE** make an issue if you have a problem or suggestion with another device so it can get sorted/added  

