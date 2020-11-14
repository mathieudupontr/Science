#résolution équation second degré :
#a*x**2+b*x+c=0

#import module
from math import sqrt
from matplotlib import pyplot as plt 
import numpy as np

#variables
a=float(input('a = '))
b=float(input('b = '))
c=float(input('c = '))
xmin=float(input('xmin = '))
xmax=float(input('xmax = '))

#calcul delta
delta=b**2-4*a*c
print('delta = '+str(delta))

#calcul racines
if delta>0 :
    x1=(-b+sqrt(delta))/(2*a)
    x2=(-b-sqrt(delta))/(2*a)
    print('x1 = '+str(x1),'x2 = '+str(x2))
    
if delta==0 :
    x0=-b/(2*a)
    print('x0 = '+str(x0))
    
if delta<0 :
      c1=(-b-complex(0,1)*sqrt(-delta))/(2*a)
      c2=(-b+complex(0,1)*sqrt(-delta))/(2*a)
      print('c1 = '+str(c1),'c2 = '+str(c2))
    
# graphe   
x=np.arange(xmin,xmax,0.001)

def équation_second_degré(a,b,c) :
    plt.plot(x,a*x**2+b*x+c)
    
    plt.title('Equation second degré : '+str(a)+'*x**2+'+str(b)+'*x+'+str(c)+'=0')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.grid(True)
    plt.show()
    
équation_second_degré(a,b,c)



























