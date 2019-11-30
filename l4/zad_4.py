# -*- coding: utf-8 -*-
"""
Created on Wed Oct 30 10:27:33 2019

@author: mateu
"""
def element_ciagu(a1,q,n):
    wynik=0
    wynik=a1*q**(n-1)
    print(wynik)
    

print("Obliczanie n-tego elementu ciągu geometrycznego")
print("Podaj wartosc pierwszego wyrazy ciagu:")
a_1=int(input())
print("Podaj wartosc iloczynu ciągu geometrycznego:")
q=int(input())
print("Który element ciągu chcesz obliczyć?\n n=")
n=int(input())
element_ciagu(a_1,q,n)