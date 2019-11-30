# -*- coding: utf-8 -*-
"""
Created on Sun Nov  3 10:07:47 2019

@author: mateu
"""

#obliczanie silni

def silnia_rek(n):
    if n==0:
        return 1
    elif n==1:
        return 1
    else:
        return n*silnia_rek(n-1)
    

print("Podaj n:")
n=int(input())
wynik=silnia_rek(n)
print(wynik)