# -*- coding: utf-8 -*-
"""
Created on Sun Nov  3 11:15:40 2019

@author: mateu
"""

#największy wspólny dzielnik

def NWD(lista_1,lista_2):
    lista_3=lista_1+lista_2 #stworzenie listy z dzielnikami obu liczb
    lista_4=[] #lista z dzielnikami, ktore sie powtarzaja
    dlugosc=len(lista_3)
    for i in range(dlugosc):
        if lista_3.count(lista_3[i])>1:
            lista_4.append(lista_3[i])
          
    lista_4_u=list(set(lista_4))
    dlugosc_2=len(lista_4_u)
    iloczyn=1
    for j in range(dlugosc_2):
        iloczyn=iloczyn*lista_4_u[j]
        
    print("NWD=",iloczyn)
    return
def czynniki_pierwsze(liczba):
    dzielniki=[]
    i=2
    while liczba>1:
        if liczba%i==0:
            dzielniki.append(i)
            print(liczba,"|",i,"\n")
            temp=liczba/i
            liczba=temp
        else:
            i+=1
    return dzielniki
         
print("Podaj liczbe a:")
a=int(input())
print("Podaj liczbe b:")
b=int(input())
print("Czynniki pierwsze liczby a:")
dzielniki_1=czynniki_pierwsze(a)
print(dzielniki_1)
print("Czynniki pierwsze liczby b:")
dzielniki_2=czynniki_pierwsze(b)
print(dzielniki_2)
NWD(dzielniki_1,dzielniki_2)
