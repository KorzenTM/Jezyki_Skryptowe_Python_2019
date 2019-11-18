# -*- coding: utf-8 -*-
"""
Created on Fri Oct 11 18:19:37 2019

@author: mateu
"""
import math
import cmath
import numpy as np

def zadanie_1():
    #input pobiera domyslnie typ string, konieczne rzutowanie na int
    a=input()
    b=input()
    suma=a+b
    print(suma)
    return
    
def zadanie_2():
    #obliczanie pola trojkata z wykorzystaniem wzoru
    a=3
    b=4
    angle=47
    #zamiana stopni na radiany
    rad=(angle*(2*math.pi))/360
    #obliczenie pola
    pole=(a*b*math.sin(rad))/2
    print("Pole trojkata wynosi:",pole)
    return
    

def zadanie_3():
    #obliczanie pola trojkata z wykorzystaniem wzoru i funkcji input
    
    print("Podaj bok a:")
    a=int(input())
    print("Podaj bok b:")
    b=int(input())
    print("Podaj kat miedzy bokami a i b(w stopniach):")
    angle=int(input())
    #zamiana stopni na radiany
    rad=float((angle*(2*math.pi))/360)
    #obliczenie pola
    pole=float((a*b*math.sin(rad))/2)
    print("Pole trojkata wynosi:",pole)
    return

def zadanie_4():
    import builtins
    dir(builtins)
    
    help(print)
    
    print("Ala ma kota")
    print(2+2)
    print(2**5,"\t",35//2,"\t",35/2,"\t",35%2)
    print(2**5,"\n",35//2,"\n",35/2,"\n",35%2)
    return
    
def zadanie_5():
    #Operacje zaokraglania
    
    dziel_bez_reszty=5//2
    print("Dzialanie //:")
    print("5//2=",dziel_bez_reszty)
    print("Funkcja math.floor():")
    #Metoda numeryczna Python floor () zwraca największa liczba całkowita nie większa niż x.
    print("math.floor(-19.21): ", math.floor(-19.21))
    print("math.floor(19.46): ", math.floor(19.46))
    print("math.floor(46.19): ", math.floor(46.19))
    print("Funkcja round();")
    #Funkcja round() zaokragla zgodnie z zasadami, można ustawić do której liczby
    print("round(-19.21): ", round(-19.21))
    print("round(19.66): ", round(19.66))
    print("round(46.19): ", round(46.19))
    return

def zadanie_6():
    a=complex(-17)
    print(a)
    pierwiastek=cmath.sqrt(a)
    print(pierwiastek)
    return

def zadanie_7():
    i=0
    
    for _ in range(5):
        print(_)
        
    return

def zadanie_8():
    print("Podaj liczbe a:")
    a=int(input())
    print("Podaj liczbe b:")
    b=int(input())
    li=[a,b]
    li.sort()
    print("Posortowane liczby:", li)
    Z=li[1]%li[0]
    print("Reszta z dzielenia:",Z)
    Z*=Z+3
    print("Wynik dzialania wynosi:",Z)
    return
    
def zadanie_9():
    print("Podaj czesc rzeczywista:")
    x=int(input())
    print("Podaj czesc urojona:")
    y=int(input())
    z=complex(x,y)
    print("Twoja liczba:",z)
    print("Arg(z)=",np.angle(z,deg=True))
    print("|z|=",abs(z))
    print("z*=",z.conjugate())
    return

def zadanie_10():
    x=0
    y=1
    z=complex(x,y)
    z1=cmath.sin(z)
    z2=cmath.cos(z)
    print("sin(z)=",z1)
    print("cos(z)=",z2)
    wynik=z1**2+z2**2
    print("sin(z)^2+cos(z)^2=",wynik)
   
#zadanie_1()
#zadanie_2()
#zadanie_3()
#zadanie_4()
zadanie_5()
#zadanie_6()
#zadanie_7() 
#zadanie_8()       
#zadanie_9()    
#zadanie_10()