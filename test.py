import tp24
col = tp24.rgb(255, 0, 0)
col2 = tp24.rgb(250, 30, 0)

m = tp24.tools.similarity(col.hsv(),col2.hsv())
n = tp24.tools.similarity(col.hsl(),col2.hsl())
print(m, n)

o = col2.analogous()
print(o)