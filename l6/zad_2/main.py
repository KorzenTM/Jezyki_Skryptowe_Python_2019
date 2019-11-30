# -*- coding: utf-8 -*-
"""
Created on Mon Nov 18 12:35:04 2019

@author: mateu
"""
import SzyfrCezara


print("Co chcesz zrobić?")
print("1. Szyfrowanie.")
print("2. Deszyfrowanie")
wybor=int(input("Wybór:"))

if wybor==1:
    napis=input("Twój napis:")
    SzyfrCezara.szyfrowanie(napis)
elif wybor==2:
    napis=input("Twój napis:")
    SzyfrCezara.deszyfrowanie(napis)
else:
    print("Zły wybór!2")