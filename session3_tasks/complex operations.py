import cmath
import math
class Complex_op:
    def __init__(self, x, y):
        cmplx= complex(x, y)
        r = cmplx.real
        img = cmplx.imag
        self.x = r
        self.y = img
    def __str__(self):
        return "{0} +{1}i".format(self.x, self.y)
    
    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Complex_op(x,y)
    def __sub__(self, other):
        x = self.x - other.x
        y = self.y - other.y
        return Complex_op(x,y)
    
    def __mul__(self, other):
        mult = complex(self.x, self.y)*complex(other.x, other.y)
        x = mult.real
        y = mult.imag
        return Complex_op(x,y)
    def __truediv__(self, other):
        divis = complex(self.x, self.y)/complex(other.x, other.y)
        x = divis.real
        y = divis.imag
        return Complex_op(x,y)
    def mod(self):
        x = self.x**2
        y = self.y**2
        modul = math.sqrt(x+y)
        return modul


a = Complex_op(3,2)
b = Complex_op(-4,-5)

print(a.mod())

        


            
        
