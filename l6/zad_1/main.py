# -*- coding: utf-8 -*-
"""
Created on Mon Nov 18 12:01:18 2019

@author: mateu
"""

import trojkat

print("Podaj boki trojkata:")
a=int(input("Bok a:")) #pierwsze ramie
b=int(input("Bok b:")) #drugie ramie
c=int(input("Bok c:")) #podstawa

#sprawdzenie warunkow istnienia trojkąta, gdzie c to podstawa,a b i a to boki
if a+b>c and a+c>b and b+c>a:
    trojkat.obwod(a,b,c)
    trojkat.pole(a,b,c)
    trojkat.rodzaj_trojkata(a,b,c)
    trojkat.kat_trojkata(a,b,c)
else:
    print("Z podanych boków nie można stworzyć trójkąta!")