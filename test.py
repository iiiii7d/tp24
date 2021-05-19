import tp24
import time

s = time.time()
col = tp24.rgb(255, 0, 0)
col2 = tp24.rgb(250, 30, 0)

o = tp24.rgb.from_web("orchid")
print(o)
print(time.time()-s)