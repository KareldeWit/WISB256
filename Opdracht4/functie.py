import bisection
import math

root = bisection.findAllRoots(lambda x: x**4 - x**2,-5,5,0.001)
print(root)