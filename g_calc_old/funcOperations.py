'''
This file is a catalog of all function operations in the form of procedures. 
Each procedure represents a new mathematical function, from which the func.py file will call to draw the respective mathematical function
'''
# imports
import math as ma
import sympy as sp

class debug():
    
    # check for imaginary
    '''https://www.programiz.com/python-programming/examples/check-string-number'''
    def isFloat(self, num):
        try:
            float(num)
            return True
        except TypeError:
            return False
        
    pass

# algebraic functions
class algebraicFuncs():
    
    # linear
    def linear(self, m, x, b):
        y = (m * x) + b
        return y

    # quadratic
    def quadratic(self, a, x, h, k):
        y = (a * ((x-h) * (x-h)) + k)
        return y

    # polynomic
    def polynomic(self):
        return

    # square root
    def squareRoot(self, a, x, h, k):
        y = (a * (sp.sqrt(x - h)) + k)
        return y
        
    # exponential
    def exponential(self, a, b, x, h, k):
        y = (a * (b) ** (x - h) + k)
        return y
    
    # logarithmic
    def log(self, a, b, x, h, k):
        y = (a * (sp.log(x, b) - h) + k)
        return y
    
    # rational
    def rational(self, a, b, x, h, k):
          y = ((b / (a * (x-h))) + k)
          return y
    
    #  absolute value
    def absolute(self, a, x, h, k):
        y = (a * (abs(x - h)) + k)
        return y
    pass

# trig functions
class trigonometricFuncs():
    
    # sine
    def sine(self, a, b, x, h, k):
        y = (a * (ma.sin((b * x) - h)) + k)
        return y
    
    # cosine
    def cosine(self, a, b, x, h, k):
        y = (a * (ma.cos((b * x) - h)) + k)
        return y
    
    # tangent
    def tangent(self, a, b, x, h, k):
        y = (a * (ma.tan((b * x) - h) + k))
        return y
    
    # cosecant
    def cosecant(self, a, b, x, h, k):
        y = (a *(1 / ma.sin(b * x) - h) + k)
        return y
    
    # secant
    def secant(self, a, b, x, h, k):
        y = (a *(1 / ma.cos(b * x) - h) + k)
        return y
    
    # cotangent
    def cotangent(self, a, b, x, h, k):
        y = (a *(1 / ma.tan(b * x) - h) + k)
        return y
    pass