import sys
import timeit

T1 = timeit.default_timer()

N = int(sys.argv[1])
output = sys.argv[2]

lijst = list(range(2, N))

for mini in lijst:
    for getal in lijst:
        if (getal%mini ==0 and getal!=mini):
            lijst.remove(getal)

primes = open(output,'w')
for getal in lijst:
    primes.write(str(getal) + "\n")
    
T2 = timeit.default_timer()

print('Found ' + str(len(lijst)) + ' Prime numbers smaller than ' +str(N) + ' in ' + str(T2-T1) + ' sec.')