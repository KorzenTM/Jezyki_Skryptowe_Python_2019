# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 18:15:42 2019

@author: mateu
"""

#szyfrowanie i deszyfrowanie

klucz_szyfrowanie={"a" : "y", "e" : "i", "i" : "o", "o" : "a", "y" : "e"}
klucz_deszyfrowanie={"y" : "a", "i" : "e", "o" : "i", "a" : "o", "e" : "y"}

def szyfrowanie(napis):
    nowy_napis=[]
    print(napis)
    for i in range(len(napis)):
        if napis[i] in klucz_szyfrowanie:
            nowy_napis.append(klucz_szyfrowanie[napis[i]])
        else:
            nowy_napis.append(napis[i])
    s=""
    s=s.join(nowy_napis)
    print(s)
    return
    
def deszyfrowanie(napis):
    nowy_napis=[]
    print(napis)
    for i in range(len(napis)):
        if napis[i] in klucz_deszyfrowanie:
            nowy_napis.append(klucz_deszyfrowanie[napis[i]])
        else:
            nowy_napis.append(napis[i])
    s=""
    s=s.join(nowy_napis)
    print(s)
    return
    



print("Co chcesz zrobić?")
print("1. Szyfrowanie.")
print("2. Deszyfrowanie.")
wybor=int(input("Twój wybór:"))

if wybor==1:
    napis=input("Podaj napis:")
    szyfrowanie(napis)
elif wybor==2:
    napis=input("Podaj napis:")
    deszyfrowanie(napis)
else:
    print("Niepoprawny wybór. Zamykanie programu...")