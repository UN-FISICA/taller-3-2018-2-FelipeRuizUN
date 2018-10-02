#!/usr/bin/python
# -*- coding: utf-8 -*-
import myfloat_func as f
class MyFloat:

    def __init__(self,num) :
        if (type(num) is float) or (type(num) is int):  
            self.num=f.tup(num)
        else:self.num=num               
    

    def __add__(self,other):
        
        if isinstance (other , MyFloat ):
            return MyFloat(f.suma(self.num,other.num))
        elif isinstance (other ,( int , float )):
            return MyFloat(f.suma(self.num,f.tup(other)))
        else: 
            return NotImplemented

    def __sub__(self,other):
        if isinstance (other , MyFloat ):
            return MyFloat(f.resta(self.num,other.num))
        elif isinstance (other ,( int , float )):
            return MyFloat(f.resta(self.num,f.tup(other)))
        else: 
            return NotImplemented

    def __mul__(self,other):
        if isinstance (other , MyFloat ):
            return MyFloat(f.multiplicacion(self.num,other.num))
        elif isinstance (other ,( int , float )):
            return MyFloat(f.multiplicacion(self.num,f.tup(other)))
        else:
            return NotImplemented

    def __truediv__(self,other):
        if isinstance (other , MyFloat ):
            return MyFloat(f.division(self.num,other.num))
        elif isinstance (other ,( int , float )):
            return MyFloat(f.division(self.num,f.tup(other)))
        else:
            return NotImplemented
        
    def __radd__(self,other):
        return self.__add__(other)

    def __rsub__(self,other):
        return self.__sub__(other)*-1
    
    def __rmul__(self,other):
        return self.__mul__(other)
    

    def __rtruediv__(self,other):
        t=MyFloat(other)
        return t/self

    def __str__(self):
        return f.imprimir(self.num)

    def __repr__(self):
        return f.imprimir(self.num)

    def __eq__(self,other):
         if isinstance (other , MyFloat ):
             return f.comparacion(self.num,other.num)
         elif isinstance (other ,( int , float )):
             return f.comparacion(self.num,f.tup(other))

    def __ne__(self,other):
        return not self.__eq__(other)
        pass
if __name__ == "__main__":
    pi=MyFloat(0)
    
    for k in range(500000000000000):
        pi=pi+(((-1)**k)/(MyFloat(2*k+1)))        
    pi=pi*4     
    while len(pi.num[1])>30:
        pi.num[1].pop(-1)
       
    print (pi) 
