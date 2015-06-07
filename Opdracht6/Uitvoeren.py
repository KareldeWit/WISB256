from lorenz import *

L1 = Lorenz([-1,1,0])
u1 = L1.solve(50,0.01)

L2 = Lorenz([8.48528, 8.48528, 27.])
print(L2.isStable([8.48528, 8.48528, 27.]))

u2 = L2.solve(50,0.01)

print(u1[0][0],u2[0][0])

print(u1[-1][0],u2[-1][0])