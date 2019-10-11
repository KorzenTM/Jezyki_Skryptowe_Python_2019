# -*- coding: utf-8 -*-
"""
Created on Wed Oct  9 08:31:53 2019

@author: mateu
"""

#obliczanie pola trojkata z wykorzystaniem wzoru i funkcji input
import math

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