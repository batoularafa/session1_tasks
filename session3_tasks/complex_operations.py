'''importing math'''
import math
class ComplexOp:
    '''class for complex numbers operation'''
    def __init__(self, input_1, input_2):
        cmplx= complex(input_1, input_2)
        r = cmplx.real
        img = cmplx.imag
        self.input_1 = r
        self.input_2 = img
    def __str__(self):
        return f"{self.input_1} +{self.input_2}i"
    def __add__(self, other):
        input_1 = self.input_1 + other.input_1
        input_2 = self.input_2 + other.input_2
        return ComplexOp(input_1,input_2)
    def __sub__(self, other):
        input_1 = self.input_1 - other.input_1
        input_2 = self.input_2 - other.input_2
        return ComplexOp(input_1,input_2)
    def __mul__(self, other):
        mult = complex(self.input_1, self.input_2)*complex(other.input_1, other.input_2)
        input_1 = mult.real
        input_2 = mult.imag
        return ComplexOp(input_1,input_2)
    def __truediv__(self, other):
        divis = complex(self.input_1, self.input_2)/complex(other.input_1, other.input_2)
        input_1 = divis.real
        input_2 = divis.imag
        return ComplexOp(input_1,input_2)
    def mod(self):
        '''modulus'''
        input_1 = self.input_1**2
        input_2 = self.input_2**2
        modul = math.sqrt(input_1+input_2)
        return modul

a = ComplexOp(3,2)
b = ComplexOp(-4,-5)
print(a.mod())
print(a+b)
