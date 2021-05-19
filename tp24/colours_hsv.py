import tp24.colour as colour
import tp24.errors as errors

class hsv(colour.Colour):
    h = None
    s = None
    v = None

    def __init__(self, vh: int, vs: int, vv: int):
        if not 0 <= vh <= 360:
            raise errors.RangeError(f"Value of H channel is {vh} but is not in range of 0 <= h <= 360")
        elif not 0 <= vs <= 100:
            raise errors.RangeError(f"Value of S channel is {vs} but is not in range of 0 <= s <= 100")
        elif not 0 <= vv <= 100:
            raise errors.RangeError(f"Value of V channel is {vv} but is not in range of 0 <= v <= 100")
        self.h = vh
        self.s = vs
        self.v = vv
    
    def __iter__(self):
        t = (self.h, self.s, self.v)
        for i in t:
            yield i

    def rgb(self):
        pass

    def hsl(self):
        pass

    def cmyk(self):
        pass

class hsva(hsv, colour.ColourAlpha):
    def __init__(self, *v):
        hsv.__init__(self, *v[:-1])
        colour.ColourAlpha.__init__(self, v[-1])

    def __iter__(self):
        t = (self.h, self.s, self.v, self.a)
        for i in t:
            yield i