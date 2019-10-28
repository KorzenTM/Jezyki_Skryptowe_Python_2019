# -*- coding: utf-8 -*-
"""
Created on Thu Oct 24 19:12:10 2019

@author: mateu
"""
#rozwiązania listy 2
import math
import re
import numpy as np

def zadanie_1():
    samogloski=('a','e','y','i','o','ą','ę','u','ó')
    spolgloski=('b','c','ć','d','f','g','h','j','k','l','m','n','p','r','s','t','w','y','z','ż','ź')
    
    print("Podaj literę:")
    litera=input()
    litera=litera.lower()
    
    if litera in samogloski:
        print("Podana litera jest samogłoską")
    elif litera in spolgloski:
        print("Podane litera jest społgloską")
    else:
        print("Niepoprawna litera")
    return

def zadanie_2_a():
    print("Podaj liczbę całkowitą")
    liczba=int(input())
    if liczba%2==0:
        print("Liczba jest parzysta")
    else:
        print("Liczba jest nieparzysta")
    return

def zadanie_2_b():
    print("Podaj liczbę całkowitą")
    liczba=int(input())
    wynik=liczba%2
    print(wynik==0)
    return

def zadanie_3():
    print("Podaj współczynniki równania(kolejno a,b,c)")
    a=int(input())
    b=int(input())
    c=int(input())
    delta=b**2-4*a*c
    if a==0:
        print("Twoje równanie nie jest rówananiem kwadratowym.")
    else:
        if delta>0:
            print("Twoja funkcja posiada dwa miejsca zerowe:")
            print("x1=",(-b-math.sqrt(delta))/2**a)
            print("x2=",(-b+math.sqrt(delta))/2**a)
        elif delta==0:
            print("Twoja funkcja posiada jedno miejsce zerowe:")
            print("x1=",-b/2*a)
        elif delta<0:
            print("Twoja funkcja nie ma miejsc zerowych.")
    return

def zadanie_4():
   L=["*    ",
      "*    ",
      "*    ",
      "*    ",
      "*    ",
      "*    ",
      "*****"]
   
   A=["      *      ",
      "     * *     ",
      "    *   *    ",
      "   *******   ",
      "  *       *  ",
      " *         * ",
      "*           *"
      ]
   
   R=["**** ",
      "*   *",
      "*   *",
      "**** ",
      "* *  ",
      "*  * ",
      "*   *"]
   for i in range(0,7):
       print(L[i]," ",A[i]," ",R[i])
   return

def zadanie_5():
    print("Podaj hasło:")
    password=input()
    pattern = "^.*(?=.{8,})(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[@#$%^&+=]).*$"
    result = re.findall(pattern, password)
    length=len(password)
    if length>6 and length<16:
        print("Hasło ma odpowiednią długosc, ")
        if (result):
            print("i jest poprawne. Dziękujemy!")
        else:
            print("ale jest niepoprawne. Podaj inne.")
    else:
        print("Hasło jest za krotkie. Podaj inne.")
    return

def zadanie_6():
    li=[]
    print("Podaj i:")
    wiersz=int(input())
    print("TABLICZKA MNOŻENIA")
    for i in range(1,wiersz+1):
        for j in range(1,11):
            print(i*j,end=" ")
            
        print()
    return

def zadanie_7():
    a=0 #pierwszy wyraz ciągu
    b=1 #drugi wyraz ciągu
    suma=0 
    wyniki=[]
    print("Podaj N:")
    N=int(input())
    print("Element 0 = ",a)
    print("Element 1 = ",b)
    for i in range(2,N+1):
        suma=a+b
        a=b
        b=suma
#        wyniki.append(suma)
        print("Element",i,"=",suma)
        
    return
        
def zadanie_8():
    
    for i in range(1,10):
        print(i*str(i))
        
    return

def zadanie_9():
    print("Podaj m:")
    m=int(input()) #wiersze
    print("Podaj n:")
    n=int(input()) #kolumny
     
    table=np.zeros((m,n),int)
    
    for i in range(0,m):
        for j in range(0,n):
            table[i][j]=i*j
            
    print(table)        
    return

def zadanie_10():
    lista=[]
    
    for i in range(100,401):
        liczba=str(i)
        a=int(liczba[0])
        b=int(liczba[1])
        c=int(liczba[2])
        
        if a%2==0 and b%2==0 and c%2==0:
            lista.append(i)
        
        
    print(lista)
            
    
    
#zadanie_1()    
#zadanie_2_a()
#zadanie_2_b()
#zadanie_3()
#zadanie_4()
#zadanie_5()
#zadanie_6()
#zadanie_7()
#zadanie_8()
#zadanie_9()
zadanie_10()