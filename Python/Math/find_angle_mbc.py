import math
ab = int(input())
bc = int(input())

ac = math.sqrt(ab**2 + bc**2)
ac_medios = ac/2
deg_c = math.asin(ab/ac)
c = math.sqrt(bc**2 + ac_medios**2 - 2*bc*ac_medios * math.cos(deg_c))

deg = str(round(math.degrees(math.asin(((ac_medios* math.sin(deg_c))/c))))) + "\u00B0"

print(deg)