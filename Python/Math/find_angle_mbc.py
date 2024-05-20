import math
ab = int(input())
bc = int(input())

ac = math.sqrt(ab**2 + bc**2) #Find side AC with pythagoras
ac_medios = ac/2 #Find the midpoint of C
deg_c = math.asin(ab/ac) #Calculate Angle C with arcsin
c = math.sqrt(bc**2 + ac_medios**2 - 2*bc*ac_medios * math.cos(deg_c)) #Finding the length of the side created by the midpoint with law of cosines
deg = str(round(math.degrees(math.asin(((ac_medios* math.sin(deg_c))/c))))) + "\u00B0" #Finding the angle MBC using law of sines

print(deg)