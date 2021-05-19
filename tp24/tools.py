import tp24.internal as internal
import tp24.colour as colour

def gradient(a: colour.Colour, b: colour.Colour, ap=0.5, bp=0.5):
    av, bv = internal.tuplify(a, b)
    new = tuple(round((p*ap+q*bp)/(ap+bp)) for p, q in zip(av, bv))
    return internal.getclass(a, b)(*new)