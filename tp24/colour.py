import importlib
import re
import tp24.internal as internal
import tp24.errors as errors
import tp24.tools as tools


class Colour:
    def __add__(self, other):
        if internal.unalpha(type(self).__name__, self) != internal.unalpha(type(other).__name__, other):
            funcname = internal.unalpha(type(self).__name__, self)
            other = getattr(other, funcname)()
        sv, ov = internal.tuplify(self, other)
        new = tuple(a+b for a, b in zip(sv, ov))
        oc = internal.getclass(self, other)
        new = tuple(c if r>=len(oc.RANGE) or c<=oc.RANGE[r] else oc.RANGE[r] for r, c in enumerate(new)) 
        return oc(*new)

    def __sub__(self, other):
        sv, ov = internal.tuplify(self, other)
        new = tuple(a-b for a, b in zip(sv, ov))
        oc = internal.getclass(self, other)
        new = tuple(c if r>=len(oc.RANGE) or c<=oc.RANGE[r] else oc.RANGE[r] for r, c in enumerate(new)) 
        return oc(*new)

    def __mul__(self, other):
        return tools.gradient(self, other)

    def __repr__(self):
        model = type(self).__name__
        vals = str(tuple(self))
        return model+vals
        
    def hexv(self, compress=False):
        if not type(self).__name__.startswith("rgb"):
            c = self.rgb()
        else:
            c = self

        r = "#"
        for i in tuple(c):
            n = hex(i).split('x')[1]
            if len(n) == 1: n = "0"+n
            r += n

        if compress:
            single = re.search(r"^#(.)\1{5}$", r)
            triple = re.search(r"^#(.)\1(.)\2(.)\3(?:(.)\4)?$", r)
            if single:
                r = "#"+single.group(1)
            elif triple:
                r = "#"
                for i in triple.groups():
                    if i != None: r += i

        return r

    @classmethod
    def from_hex(cls, hexc: str):
        c = re.search(r"#(.+)", hexc)
        if not c or not len(c.group(1)) in [1, 3, 4, 6, 8]:
            raise ValueError(f"Hex {hexc} not a valid hex")

        if len(c.group(1)) == 1:
            c = c.group(1)*6
        elif len(c.group(1)) in [3, 4]:
            c = ''.join([char*2 for char in c.group(1)])
        else:
            c = c.group(1)

        channels = tuple(c[i:i+2] for i in range(0, len(c), 2))
        channels = tuple(int('0x'+i, 16) for i in channels)

        import tp24.colours_rgb as col_rgb

        if issubclass(cls, ColourAlpha):
            channels = list(channels)
            channels[3] *= 100/255
            channels[3] = round(channels[3])
            channels = tuple(channels)
            colour_rgb = col_rgb.rgba(*channels)
        else:
            colour_rgb = col_rgb.rgb(*channels)
        
        if not cls.__name__.startswith("rgb"):
            classname = internal.unalpha(cls.__name__, cls)
            return getattr(colour_rgb, classname)()
        else:
            return colour_rgb

    def inverted(self):
        old = internal.unalpha(tuple(self), self)
        new = tuple(a-b for a, b in zip(self.RANGE, old))
        if issubclass(type(self), ColourAlpha): new = tuple(list(new)+[self.a])

        return type(self)(*new)
            

    def add_alpha(self, va: int):
        if issubclass(type(self), ColourAlpha):
            return self
        classname = type(self).__name__+'a'
        modulename = type(self).__name__
        module = importlib.import_module("tp24.colours_"+modulename)
        vals = tuple(list(self)+[va])
        return getattr(module, classname)(*vals)
    
class ColourAlpha:
    def __init__(self, va: int):
        if va != None and not 0 <= va <= 100:
            raise errors.RangeError(f"Value of A channel is {va} but is not in range of 0 <= a <= 100")
        self.a = va

    def remove_alpha(self):
        classname = type(self).__name__[:-1]
        modulename = type(self).__name__[:-1]
        module = importlib.import_module("tp24.colours_"+modulename)
        vals = tuple(list(self)[:-1])
        return getattr(module, classname)(*vals)