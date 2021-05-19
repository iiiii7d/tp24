import tp24.colour as colour
import tp24.colours_rgb as col_rgb
import tp24.errors as errors

class cmyk(colour.Colour):
    c = None
    m = None
    y = None
    k = None

    def __init__(self, vc: int, vm: int, vy: int, vk: int):
        if not 0 <= vc <= 100:
            raise errors.RangeError(f"Value of C channel is {vc} but is not in range of 0 <= C <= 100")
        elif not 0 <= vm <= 100:
            raise errors.RangeError(f"Value of M channel is {vm} but is not in range of 0 <= m <= 100")
        elif not 0 <= vy <= 100:
            raise errors.RangeError(f"Value of Y channel is {vy} but is not in range of 0 <= y <= 100")
        elif not 0 <= vk <= 100:
            raise errors.RangeError(f"Value of K channel is {vk} but is not in range of 0 <= k <= 100")
        self.c = vc
        self.m = vm
        self.y = vy
        self.k = vk
    
    def __iter__(self):
        t = (self.c, self.m, self.y, self.k)
        for i in t:
            yield i

    def rgb(self):
        r = 255 * (100-self.c) * (100-self.k)
        g = 255 * (100-self.m) * (100-self.k)
        b = 255 * (100-self.y) * (100-self.k)

        r = round(r)
        g = round(g)
        b = round(b)

        if issubclass(type(self), colour.ColourAlpha):
            return col_rgb.rgba(r, g, b, self.a)
        else:
            return col_rgb.rgb(r, g, b)

    def hsl(self):
        pass

    def hsv(self):
        pass

class cmyka(cmyk, colour.ColourAlpha):
    def __init__(self, *v):
        cmyk.__init__(self, *v[:-1])
        colour.ColourAlpha.__init__(self, v[-1])

    def __iter__(self):
        t = (self.c, self.m, self.y, self.k, self.a)
        for i in t:
            yield i