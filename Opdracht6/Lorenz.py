from scipy.integrate import odeint
from numpy import linspace,arange

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
    
    