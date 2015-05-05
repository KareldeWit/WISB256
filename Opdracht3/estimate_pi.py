import random
import math
import sys

# random trekkingen
def randline():
    x0 = random.random()
    a = random.vonmisesvariate(0,0)
    x1 = x0+l*math.sin(a)
    
    if math.floor(x0) != math.floor(x1):
        return 1
    return 0

# initialisatie
if len(sys.argv) <= 2:
    print("Use: estimate_pi.py N L")
    sys.exit()

end = int(sys.argv[1])
l = int(sys.argv[2])

if (l<0 or l>1):
    print("AssertionError: L should be smaller than 1")
    sys.exit()

if len(sys.argv) == 4:
    seed = int(sys.argv[3])
    random.seed(seed)

# main    
i = 0
h = 0

while i<end:
    h += randline()
    i += 1
approx = (2*l*end)/float(h)

print(str(h) + " hits in " + str(end) + " tries")
print("Pi = " + str(approx))