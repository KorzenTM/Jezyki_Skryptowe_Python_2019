# -*- coding: utf-8 -*-
"""
Created on Thu Oct 17 18:00:25 2019

@author: mateu
"""

import math
import itertools

def zadanie_1():
    
    print(20*(str(1.2E+3+34.5)+";"))
    return

def zadanie_2():
    napis=input()
    print(30*(napis+"\n"))
    return

def zadanie_3():
    napis=input()
    dlugosc=len(napis)
    print(napis[0:2]+napis[dlugosc-2:])
    return

def zadanie_4():
    napis=input()
    napis_2=napis[1:]
    pierwsza=napis[0]
    print(pierwsza+napis_2.replace(pierwsza,"$"))
    return
    
def zadanie_5():
    print("Podaj napis:")
    napis=input()
    dlugosc=len(napis)
    polowa=dlugosc//2
    print(polowa)
    print(napis)
    print(napis[:polowa]+"Python"+napis[polowa:])
    return

def zadanie_6():
    print("Lista studentow:")
    studenci=["Kasia","Basia","Marek","Darek"]
    print(studenci)
    studenci.append("Józek")
    print("Dodanie Józka:")
    print(studenci)
    dodatkowi=["Ania","Basia"]
    studenci.extend(dodatkowi)
    print("Dodanie Anii i Basii:")
    print(studenci)
    print("Posortowanie alfabetyczne:")
    studenci.sort()
    print(studenci)
    print("Wyswietlenie czwartego studenta:")
    print(studenci[3])
    print("Wyswietlenie dwoch pierwszych:")
    print(studenci[0:2])
    dlugosc=len(studenci)
    print("Wyswietlenie dwoch ostatnich:")
    print(studenci[dlugosc-2:])
    print("Usuniecie Basii:")
    while "Basia" in studenci:
        studenci.remove("Basia")
        
    print(studenci)
    dlugosc_2=len(studenci)
    print("Pozostala liczba studentow:",dlugosc_2)
    studenci_krotka=tuple(studenci)
    print(studenci_krotka)
    return
 
def zadanie_7():
    lista_1=[(2,5),(1,2),(4,4)]
    lista_2=[(2,8),(5,5),(9,3),(1,0),(3,2),(6,4),(1,9),(10,3),(2,3),(1,7)]
    print("Listy przed posortowaniem:\n",lista_1,"\n",lista_2)
    print("Lista 1 posortowana po drugim elemencie:",sorted(lista_1, key=lambda lista_1:lista_1[1]))
    print("Lista 2 posortowana po drugim elemencie:",sorted(lista_2, key=lambda lista_2:lista_2[1]))
    return

def zadanie_8():
    lista=["m","a","t","e","u","s","z"]
    print(lista)
    s="" #separator, ktory laczy elementy listy
    s=s.join(lista)
    print(s)
    return

def zadanie_9():
    lista_1=[[2,5],[1,2],[4,4]]
    lista_2=[[2,4,3],[1,5,6],[7,9,0]]
    lista_1_c=list(itertools.chain.from_iterable(lista_1))
    lista_2_c=list(itertools.chain.from_iterable(lista_2))
    print("Listy przed obnizenie stopnia zagniezdzenia:\n",lista_1,"\n",lista_2)
    print("Listy przed obnizenie stopnia zagniezdzenia:\n",lista_1_c,"\n",lista_2_c)
    return

def zadanie_10():
    nums=[]
    i=1
    start=4
    for x in range(3,100,3*i):
        nums.append(x)
        i+1
        
    print("Lista:")
    print(nums)
    dlugosc=len(nums)
#    print(dlugosc)
    
    while start<=dlugosc:
        del nums[start]
        start=(start+3)-1
        dlugosc=len(nums)
#    print(dlugosc)
    print("Lista po usunieciu co trzeciego elementu:")    
    print(nums)
    suma=sum(nums)
    print("Suma elementow listy wynosi:",suma)
    return

#zadanie_1()
#zadanie_2() 
#zadanie_3()
#zadanie_4()
#zadanie_5()
#zadanie_6()
#zadanie_7()
#zadanie_8()
#zadanie_9()
zadanie_10()