# -*- coding: utf-8 -*-
"""
Created on Wed Oct 30 08:40:17 2019

@author: mateu
"""


lista=[1,2,3,4,5,6,7,8,9,10]
dlugosc=len(lista)
suma=0
iloczyn=1
    
for i in range(0,dlugosc):
    suma=suma+lista[i]
    iloczyn=iloczyn*lista[i]
        
print("Suma elementow tablicy jest rowna:",suma)
print("Suma elementow tablicy jest rowna:",iloczyn)


  
        