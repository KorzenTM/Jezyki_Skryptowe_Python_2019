# -*- coding: utf-8 -*-
"""
Created on Mon Nov 18 12:01:48 2019

@author: mateu
"""
import math

def obwod(a,b,c):
    print("Obwód trojkąta o takich bokach wynosi:",a+b+c)
    return

def pole(a,b,c):
    p=(a+b+c)/2 #polowa obwodu
    P=math.sqrt(p*(p-a)*(p-b)*(p-c)) #wzór Herona
    print("Pole trójkąta o takich bokach wynosi:",P)
    return

def rodzaj_trojkata(a,b,c):
    if a==b==c:
        print("Trójkąt jest równoboczny")
    elif a == b:
        print("Trójkąt jest równoramienny")
    elif a != b != c:
        print("Trójkąt jest różnoboczny")
    return

def kat_trojkata(a,b,c):
    if a**2+b**2==c**2:
        print("Trójkąt jest prostokątny.")
    elif a**2+b**2<c**2:
        print("Trójkąt jest rozwartokątny.")
    elif a**2+b**2>c**2:
        print("Trójkąt jest ostrokątny.")
    return
    

    
    
    