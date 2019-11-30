# -*- coding: utf-8 -*-
"""
Created on Sat Nov  2 09:35:49 2019

@author: mateu
"""

#Trójkąt pascala

def wypisz(list):
    print(str(list).center(20))


a=[1] #wartosci w trojkacie pascala
print("Podaj n")
n=int(input())
wypisz(a)
for i in range(n-1): #petla sterujaca rzedami
    temp_a=[1] #tymczasowa tablica
    for j in range(len(a)-1):
        temp_a.append(a[j]+a[j+1])
    temp_a.append(1)
    a=temp_a
    wypisz(a)


    
        
        
        