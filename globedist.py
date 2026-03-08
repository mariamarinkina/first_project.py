import sys
import math

r = 6378.137

phi1 = math.radians(float(sys.argv[1]))
l1 = float(sys.argv[2])
phi2 = math.radians(float(sys.argv[3]))
l2 = float(sys.argv[4])

dif = math.radians(abs(l1 - l2))

sig = round(r * math.atan2(math.sqrt((math.cos(phi2) * math.sin(dif))**2 + (math.cos(phi1) * math.sin(phi2) - math.sin(phi1) * math.cos(phi2) * math.cos(dif))**2), math.sin(phi1) * math.sin(phi2) + math.cos(phi1) * math.cos(phi2) * math.cos(dif)))
print(sig)