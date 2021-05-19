import tp24.colour as colour
import tp24.errors as errors
import tp24.colours_rgb as col_rgb
import tp24.colours_hsl as col_hsl

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
        h = self.h if self.h != 360 else 0
        s = self.s/100
        v = self.v/100
        c = v*s
        x = c * (1 - abs((h/60)%2 - 1))
        m = v-c

        if 0 <= h < 60:      r, g, b = c, x, 0
        elif 60 <= h < 120:  r, g, b = x, c, 0
        elif 120 <= h < 180: r, g, b = 0, c, x
        elif 180 <= h < 240: r, g, b = 0, x, c
        elif 240 <= h < 300: r, g, b = x, 0, c
        elif 300 <= h < 360: r, g, b = c, 0, x

        r = round((r+m)*255)
        g = round((g+m)*255)
        b = round((b+m)*255)

        if issubclass(type(self), colour.ColourAlpha):
            return col_rgb.rgba(r, g, b, self.a)
        else:
            return col_rgb.rgb(r, g, b)

    def hsl(self):
        h = self.h
        s = self.s/100
        v = self.v/100

        l = v - (v*s)/2
        if l in [0, 1]: s = 0
        else: s = 2-(2*l)/v

        s = round(s*100)
        l = round(l*100)

        if issubclass(type(self), colour.ColourAlpha):
            return col_hsl.hsla(h, s, l, self.a)
        else:
            return col_hsl.hsl(h, s, l)

    def cmyk(self):
        return self.rgb().cmyk()

class hsva(hsv, colour.ColourAlpha):
    def __init__(self, *v):
        hsv.__init__(self, *v[:-1])
        colour.ColourAlpha.__init__(self, v[-1])

    def __iter__(self):
        t = (self.h, self.s, self.v, self.a)
        for i in t:
            yield i