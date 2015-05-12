import bisection
import math

root = bisection.findAllRoots(lambda x: x**2-4,-4,3,0.1)
print(root)