# tp24
Python colour library, made by 7d
- supports RGB, CMY, CMYK, HSV, HSL models & transparency
- add & subtract colours to lighten & darken
- find gradient of line with proportions
- find similarity of colours
- colour schemes: analogous, complementary, compound, triadic, tetradic
  - you can define more schemes too, given degree around wheel and number of colours
- get hex of colour
- get colour from hex or web name

**Current version: v1.0**

**Documentation: https://tp24.readthedocs.io/en/latest/**

## Why 'tp24'?
tp24 stands for **t**wo **p**ower **24**, or 2^24 which equals to 16777216, the number of colours that the RGB model can show.

## Examples

### Create a colour:
```python
>>> col = tp24.rgb(255, 0, 0)
>>> col
rgb(255, 0, 0)
```

### Convert colour from one model to another
```python
>>> col = tp24.rgb(255, 0, 0)
>>> col.hsv()
hsv(0, 100, 100)
>>> col.cmyk()
cmyk(0, 100, 100, 0)
```

### Get individual channels of colour
```python
>>> col.r
255
>>> col.g
0
>>> col.b
0
```

### Get hex value of colours
```python
>>> col.hexv()
'#ff0000'
>>> col.hexv(compress=True)
'#f00'
```

### Load colour from hex or web name
```python
>>> tp24.rgb.from_hex("#987654")
rgb(152, 118, 84)
>>> tp24.hsv.from_web("orange")
hsv(39, 100, 100)
```

### Lighten and darken colours by addition & subtraction
```python
>>> col1 = tp24.rgb(255, 0, 0)
>>> col2 = tp24.hsl(270, 100, 50)
>>> col + col2
rgb(255, 0, 255)
>>> col - col2
rgb(127, 0, 0)
```

### Mix colours
```python
>>> col1*col2
rgb(192, 0, 128)
>>> tp24.tools.gradient(col1, col2)
rgb(192, 0, 128)
>>> tp24.tools.gradient(col1, col2, ap=0.25, bp=0.75)
rgb(160, 0, 191)
```

### Find similarity of colours
```python
>>> # works best in hsl/hsv
>>> col1 = tp24.hsl.from_web("red")
>>> col2 = tp24.hsl.from_web("orange")
>>> tp24.tools.similarity(col1, col2)
0.7388888888888889
>>> col2 = tp24.hsl.from_web("green")
>>> tp24.tools.similarity(col1, col2)
0.8055555555555557
```

### Colour schemes
```python
>>> col = tp24.rgb(255, 0, 0)
>>> col.analogous()
(rgb(255, 0, 128), rgb(255, 128, 0))
>>> col.compound()
(rgb(0, 255, 128), rgb(0, 128, 255))
>>> col.complementary()
rgb(0, 255, 255)
>>> col.triadic()
(rgb(0, 0, 255), rgb(0, 255, 0))
>>> col.tetradic()
(rgb(128, 0, 255), rgb(128, 255, 0), rgb(0, 255, 255))
>>> col.wheel(5, 72)
(rgb(204, 0, 255), rgb(204, 255, 0), rgb(0, 102, 255), rgb(0, 255, 102), rgb(0, 255, 102))
```

### Invert values
```python
>>> col.inverted()
rgb(0, 255, 255)
```

### Support for transparency
```python
>>> col
rgb(255, 0, 0
>>> col = col.add_alpha(50)
>>> col
rgba(255, 0, 0, 50)
>>> col = col.remove_alpha()
>>> col
rgb(255, 0, 0)
```