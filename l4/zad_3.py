# -*- coding: utf-8 -*-
"""
Created on Wed Oct 30 10:10:34 2019

@author: mateu
"""
import math

def konwersja(wybor,wartosc):
    if wybor==1:
        print("Twój kat w radianach to:",math.radians(wartosc))
    elif wybor==2:
        print("Twój kąt w stopniach to:",math.degrees(wartosc))
    else:
        print("Nie ma takiej opcji!")
    return

print("PROGRAM DO KONWERSJI")
print("Co chcesz zrobić?")
print("1 - stopnie na radiany")
print("2 - radiany na stopnie")
wybor=int(input())
print("Podaj wartosc kata:")
kat=float(input())
konwersja(wybor,kat)