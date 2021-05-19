import tp24.colour as colour
import tp24.errors as errors

class hsl(colour.Colour):
    h = None
    s = None
    l = None

    def __init__(self, vh: int, vs: int, vl: int):
        if not 0 <= vh <= 360:
            raise errors.RangeError(f"Value of H channel is {vh} but is not in range of 0 <= h <= 360")
        elif not 0 <= vs <= 100:
            raise errors.RangeError(f"Value of S channel is {vs} but is not in range of 0 <= s <= 100")
        elif not 0 <= vl <= 100:
            raise errors.RangeError(f"Value of L channel is {vl} but is not in range of 0 <= l <= 100")
        self.h = vh
        self.s = vs
        self.l = vl
    
    def __iter__(self):
        t = (self.h, self.s, self.l)
        for i in t:
            yield i

    def rgb(self):
        pass

    def hsv(self):
        pass

    def cmyk(self):
        pass

class hsla(hsl, colour.ColourAlpha):
    def __init__(self, *v):
        hsl.__init__(self, *v[:-1])
        colour.ColourAlpha.__init__(self, v[-1])

    def __iter__(self):
        t = (self.h, self.s, self.l, self.a)
        for i in t:
            yield i