import copy
import math

class Vector:
    vector = []

    #standaardfucnties
    def __init__(self, size, value=0):
        self.size = int(size)
        if isinstance(value,list):
            #print('A')
            self.vector = value
        else:
            self.vector = [value]*size
            #print('B')
    
    def __str__(self):
        output = ""
        for i in range(0,self.size-1):
            output += str(self.vector[i]) + "\n"
        output += str(self.vector[self.size-1])
        return output
            
    # Eigen functies
    def scalar(self,alpha):
        return Vector(self.size, list(map(lambda x:x*alpha,self.vector)))
        
    def lincomb(self,other,alpha,beta):
        return Vector(self.size,list(map(lambda x, y: x + y, self.scalar(alpha).vector, other.scalar(beta).vector)))
        
    def inner(self, other):
        return sum(list(map(lambda x, y: x * y, self.vector, other.vector)))

    def norm(self):
        return math.sqrt(self.inner(self))