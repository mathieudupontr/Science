## TP1 

# #exercice 1 :
# a=str(input('Nom : '))
# b=str(input('Prénom : '))
# c=int(input('Année Naissance : '))
# d=2020-c
# e=str(input('Sexe : '))
# while e!='homme'and e!='homme':
#     e=str(input('Sexe : '))
#     if str(e)=='homme':
#         print('Bonjour Mr. '+str(b)+' '+str(a)+', vous avez '+str(d)+' ans.')
#     if str(e)=='femme':
#         print('Bonjour Mme. '+str(b)+' '+str(a)+', vous avez '+str(d)+' ans.')  

#exercice 2 :
# a=float(input('1er nombre : '))
# b=float(input('2ème nombre : '))
# c=input('opération : ')

# if str(c)=='+':
#     print(a+b)
# if str(c)=='-':
#     print(a-b)
# if str(c)=='x':
#     print(a*c)
# if str(c)=='/':
#     if b!=0 :
#         print(a/b)
#     else :
#         print('erreur')
       
#exercice 3 :
# from random import randint
# a=randint(1,6)
# print(a)
# if a>=4 :
#     print('GAGNE')
# else :
#     print('PERDU')

#exercice 4 :
# a=float(input('1er nombre : '))
# b=float(input('2ème nombre : '))
# c=float(input('3ème nombre : '))
# maxi=0
# if a<b :
#     maxi=b
# else:
#     maxi=a
# if maxi<c:
#     maxi=c

# print(maxi)

#exercice 5 :
# a=int(input('saisir un nombre entier entre 1 et 26 : '))
# l=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

# print('lettre :',l[a-1])

#exercice 6 :

# #résolution équation second degré :
# #a*x**2+b*x+c=0

# #import module
# from math import sqrt
# from matplotlib import pyplot as plt 
# import numpy as np

# #variables
# a=float(input('a = '))
# b=float(input('b = '))
# c=float(input('c = '))
# xmin=float(input('xmin = '))
# xmax=float(input('xmax = '))

# #calcul delta
# delta=b**2-4*a*c
# print('delta = '+str(delta))

# #calcul racines
# if delta>0 :
#     x1=(-b+sqrt(delta))/(2*a)
#     x2=(-b-sqrt(delta))/(2*a)
#     print('x1 = '+str(x1),'x2 = '+str(x2))
    
# if delta==0 :
#     x0=-b/(2*a)
#     print('x0 = '+str(x0))
    
# if delta<0 :
#       c1=(-b-complex(0,1)*sqrt(-delta))/(2*a)
#       c2=(-b+complex(0,1)*sqrt(-delta))/(2*a)
#       print('c1 = '+str(c1),'c2 = '+str(c2))
    
# # graphe   
# x=np.arange(xmin,xmax,0.001)

# def équation_second_degré(a,b,c) :
#     plt.plot(x,a*x**2+b*x+c)
    
#     plt.title('Equation second degré : '+str(a)+'*x**2+'+str(b)+'*x+'+str(c)+'=0')
#     plt.xlabel('x')
#     plt.ylabel('f(x)')
#     plt.grid(True)
#     plt.show()
    
# équation_second_degré(a,b,c)

#exercice 7 :
# v0=1
# u=0
# v=0
# for i in range(1,11):
#     u=u+2**i
# print('somme 1 à 10 Un',u)
    
# for i in range(1,11):
#     v=v+v0*2**i
# print('somme 1 à 10 Vn :',v)

#exercice 8 :
# def factorielle(n):
#     x=1
#     for i in range (0,n):
#         x=x*(i+1)
#     return x

# a=int(input('saisir nombre : '))
# print(factorielle(a))

#exercice 9 :
from math import exp
from math import pi
print(exp(1))
print(pi)

e=0
p=0

def factorielle(n):
     x=1
     for i in range (0,n):
         x=x*(i+1)
     return x

for i in range(0,1000):
    e=e+(1/factorielle(i))
print('e =',e)
    
for i in range(0,100000):
    p=p+(((-1)**i)/(2*i+1))
print('pi =',4*p)

#exercice 10 :
#a=int(input('saisissez un nombre entier : '))

#exercice 11 :
# from random import randint
# a=randint(1,100)
# b=0
# while b!=a :
#     b=int(input('votre nombre : '))
#     if b>a :
#         print('TROP GRAND')
#     if b<a:
#         print('TROP PETIT')
#     if b==a:
#         print('GAGNE')
       
#exercice 12 :
# from math import exp
# from math import pi
# a=float(input('partie réelle : '))
# b=float(input('partie imaginaire : '))
# n=int(input('racine nème : '))
# r=0
# d=a**(1/n)
# print(d)

# for i in range(1,n+1) :
#     r=exp(complex(0,(2*i*pi)/n))
#     print(r)


























