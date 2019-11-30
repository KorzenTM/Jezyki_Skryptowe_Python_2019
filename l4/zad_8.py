# -*- coding: utf-8 -*-
"""
Created on Sun Nov  3 09:55:19 2019

@author: mateu
"""

#suma szeregu harmoniczego

suma=0
print("Podaj n:")
n=int(input())


for i in range(1,n+1):
    suma=suma+(1.0/i)
    
print(suma)