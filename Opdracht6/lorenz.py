from scipy.integrate import odeint
from numpy import *

class Lorenz:
    sig = 10.
    rho = 28.
    bet = 8./3.
    
    #contructor
    def __init__(self, init):
        self.init = init
   
    #afgeleide functie
    def f(self, z, time):
        return [self.sig * (z[1] - z[0]), 
        (z[0] * (self.rho - z[2])) - z[1], 
        (z[0] * z[1]) - (self.bet * z[2])]
       
    # Solver         
    def solve(self, T, dt):
        return odeint(self.f, self.init, arange(0,T,dt))
    
    def df(self, u):
        matrix = array( [ (-self.sig,self.sig,0), (self.rho-u[2],-1,-u[0]), (u[1],u[0],-self.bet) ] )
        return matrix
    
    # Bonus    
    def isStable(self, u):
        matrix = self.df(u)
        stable = True
        for i in linalg.eigvals(matrix):
            if i>0:
                stable = False
                break

        return stable