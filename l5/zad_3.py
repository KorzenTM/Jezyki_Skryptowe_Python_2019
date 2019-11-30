# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 17:00:26 2019

@author: mateu
"""

#zamiana liczby rzymskiej na arabską

system_rzymski={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}

def zamiana(liczba):
    dlugosc=len(liczba)
    wynik=0
    
    for i in range(dlugosc):
        if i>0 and system_rzymski[liczba[i]]>system_rzymski[liczba[i-1]]:
            wynik=wynik+system_rzymski[liczba[i]]-2*system_rzymski[liczba[i-1]]
        else:
            temp=system_rzymski[liczba[i]]
            wynik=wynik+temp
    print(wynik)
    return

print("Podaj liczbe rzymską:")
liczba=input("Twoja liczba:")
zamiana(liczba)