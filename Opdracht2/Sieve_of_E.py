import sys
import timeit
import math

# initialisatie
T1 = timeit.default_timer()
N = int(sys.argv[1])
amount = 0
output = sys.argv[2]

# aanmaken van de lijsten
priemgetallen = list(range(2, N))
delers = list(range(3,int(math.sqrt(N)),2))
delers.insert(0, 2)

#Bepalen van de priemgetallen
for deler in delers:
    for getal in priemgetallen[(deler**2)-2:N-1]:
        if (getal%deler ==0 and getal!=deler):
            priemgetallen[getal-2]=0

# Schrijven naar outputnaam
primes = open(output,'w')
for getal in priemgetallen:
    if(getal != 0):
        amount += 1
        primes.write(str(getal) + "\n")

# Einde tijdregistratie    
T2 = timeit.default_timer()

print('Found ' + str(amount) + ' Prime numbers smaller than ' +str(N) + ' in ' + str(T2-T1) + ' sec.')