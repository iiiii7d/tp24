import tp24.internal as internal

def gradient(a: 'Colour', b: 'Colour', ap=0.5, bp=0.5):
    av, bv = internal.tuplify(a, b)
    new = tuple(round((p*ap+q*bp)/(ap+bp)) for p, q in zip(av, bv))
    return internal.getclass(a, b)(*new)
