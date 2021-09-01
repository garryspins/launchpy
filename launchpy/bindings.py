
bind_methods = {
    "press": 127,
    "release": 0
}

class BindingHandler:

    # Internal Methods
    bindings = []
    def __init__(self, launchpad):
        self.launchpad = launchpad
        self.launchpad.AddEvent(self.EventHandle, (self.bindings))

    @staticmethod
    def EventHandle(lp, buttons, binds):
        if buttons == []: return

        for x in binds:
            if (x.x == buttons[0]) and (x.y == buttons[1]) and (bind_methods[x.method] == buttons[2]):
                x.func(lp, x)

    # Binding Class
    def Binding(self, x, y, silent=False, method="release", color=False):
        bind = self.__internal__Binding(x, y, silent=silent, method=method)
        bind.parent = self
        self.bindings.append(bind)

        if color:
            print(color)
            self.launchpad.SetColor(color.get("x"), color.get("y"), color.get("r"), color.get("g"), color.get("b"))

        return bind

    class __internal__Binding:
        def __init__(self, x, y, silent=False, method="release"):
            self.x = x
            self.y = y
            self.silent = silent
            self.method = method
        
        def __call__(self, f):
            self.func = f
            if not self.silent: print("Added Binding At (" + str(self.x) + ", " + str(self.y) + ") named '" + f.__name__ + "'")

    
    # Helpers
    def PreDefColor(self, x, y, color=False):
        if color:
            color["x"] = x
            color["y"] = y
            return color
        else:
            return color

    ## Mk2 Helpers
    def Mk2Up(self, color=False, silent=False, method="release"): return self.Binding(0, 0, silent=silent, color=self.PreDefColor(0, 0, color), method=method)
    def Mk2Down(self, color=False, silent=False, method="release"): return self.Binding(1, 0, silent=silent, color=self.PreDefColor(1, 0, color), method=method)
    def Mk2Left(self, color=False, silent=False, method="release"): return self.Binding(2, 0, silent=silent, color=self.PreDefColor(2, 0, color), method=method)
    def Mk2Right(self, color=False, silent=False, method="release"): return self.Binding(3, 0, silent=silent, color=self.PreDefColor(3, 0, color), method=method)
    def Mk2Session(self, color=False, silent=False, method="release"): return self.Binding(4, 0, silent=silent, color=self.PreDefColor(4, 0, color), method=method)
    def Mk2User1(self, color=False, silent=False, method="release"): return self.Binding(5, 0, silent=silent, color=self.PreDefColor(5, 0, color), method=method)
    def Mk2User2(self, color=False, silent=False, method="release"): return self.Binding(6, 0, silent=silent, color=self.PreDefColor(6, 0, color), method=method)
    def Mk2Mixer(self, color=False, silent=False, method="release"): return self.Binding(7, 0, silent=silent, color=self.PreDefColor(7, 0, color), method=method)
    
    def Mk2Volume(self, color=False, silent=False, method="release"): return self.Binding(8, 1, silent=silent, color=self.PreDefColor(8, 1, color), method=method)
    def Mk2Pan(self, color=False, silent=False, method="release"): return self.Binding(8, 2, silent=silent, color=self.PreDefColor(8, 2, color), method=method)
    def Mk2SendA(self, color=False, silent=False, method="release"): return self.Binding(8, 3, silent=silent, color=self.PreDefColor(8, 3, color), method=method)
    def Mk2SendB(self, color=False, silent=False, method="release"): return self.Binding(8, 4, silent=silent, color=self.PreDefColor(8, 4, color), method=method)
    def Mk2Stop(self, color=False, silent=False, method="release"): return self.Binding(8, 5, silent=silent, color=self.PreDefColor(8, 5, color), method=method)
    def Mk2Mute(self, color=False, silent=False, method="release"): return self.Binding(8, 6, silent=silent, color=self.PreDefColor(8, 6, color), method=method)
    def Mk2Solo(self, color=False, silent=False, method="release"): return self.Binding(8, 7, silent=silent, color=self.PreDefColor(8, 7, color), method=method)
    def Mk2RecordArm(self, color=False, silent=False, method="release"): return self.Binding(8, 8, silent=silent, color=self.PreDefColor(8, 8, color), method=method)


