import tp24
col = tp24.rgb(204, 204, 0)
col2 = tp24.rgb(255, 255, 0)

col = col.hsl().hsv().cmyk()
print(col)