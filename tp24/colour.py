import importlib
import re
import tp24.internal as internal
import tp24.errors as errors
import tp24.tools as tools

class Colour:
    def __add__(self, other):
        sv, ov = internal.tuplify(self, other)
        new = tuple(a+b if a+b<=255 else 255 for a, b in zip(sv, ov))
        return internal.getclass(self, other)(*new)

    def __sub__(self, other):
        sv, ov = internal.tuplify(self, other)
        new = tuple(a-b if a-b>=0 else 0 for a, b in zip(sv, ov))
        return internal.getclass(self, other)(*new)

    def __mul__(self, other):
        return tools.gradient(self, other)

    def __repr__(self):
        model = type(self).__name__
        vals = str(tuple(self))
        return model+vals
        
    def hexv(self, compress=False):
        if type(self).__name__ != "rgb":
            pass

        r = "#"
        for i in tuple(self):
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
    def from_hex(cls, hexv):
        pass

    def invert(self):
        if type(self).__name__.startswith("rgb"): m = (255, 255, 255)
        elif type(self).__name__.startswith("hs"): m = (360, 100, 100)
        elif type(self).__name__.startswith("cmyk"): m = (100, 100, 100, 100)
        # dont worry will unhardcopy this
        old = tuple(self)[:-1] if issubclass(type(self), ColourAlpha) else tuple(self)
        new = tuple(a-b for a, b in zip(m, old))

        for n, a in enumerate(type(self).__name__):
            setattr(self, a, new[n])
            

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