import tp24
import time

s = time.time()

print(time.time()-s)

def test_pytest():
    # inits
    col_rgba = tp24.rgba(255, 128, 204, 100)
    col_cmya = tp24.cmya(255, 128, 204, 100)
    col_hsva = tp24.hsva(100, 50, 36, 100)
    col_hsla = tp24.hsla(340, 42, 53, 100)
    col_cmyka = tp24.cmyka(100, 86, 26, 0, 100)

    col_hex = tp24.rgb.from_hex("#f00")
    col_web = tp24.rgb.from_web("red")

    # conversion
    col_rgba.cmy()
    col_rgba.hsv()
    col_rgba.hsl()
    col_rgba.cmyk()

    col_cmya.rgb()
    col_cmya.hsv()
    col_cmya.hsl()
    col_cmya.cmyk()

    col_hsva.rgb()
    col_hsva.cmy()
    col_hsva.hsl()
    col_hsva.cmyk()

    col_hsla.rgb()
    col_hsla.cmy()
    col_hsla.hsv()
    col_hsla.cmyk()

    col_cmyka.rgb()
    col_cmyka.cmy()
    col_cmyka.hsv()
    col_cmyka.hsl()

    # tools
    print(col_rgba + col_cmya)
    print(col_rgba - col_cmya)
    print(col_rgba * col_cmya)
    print(tp24.tools.similarity(col_hsva, col_hsla))
    print(tp24.tools.similarity(col_rgba, col_cmyka))

    # schemes
    col_rgba.analogous()
    col_rgba.compound()
    col_rgba.complementary()
    col_rgba.triadic()
    col_rgba.tetradic()
    col_rgba.inverted()

    # alpha
    col_rgba.remove_alpha().add_alpha(100)

    # iter
    print(tuple(col_rgba))
    print(tuple(col_cmya))
    print(tuple(col_hsva))
    print(tuple(col_hsla))
    print(tuple(col_cmyka))

test_pytest()