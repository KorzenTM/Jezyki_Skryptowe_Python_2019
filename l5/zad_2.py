# -*- coding: utf-8 -*-
"""
Created on Tue Nov 12 19:20:37 2019

@author: mateu
"""
#program zamieniający liczby dziesietne na wartosci słowne
jednosci=["","jeden","dwa","trzy","cztery","piec","szesc","siedem","osiem","dziewiec","dziesiec"]
wyjatkowe=["","jedenascie","dwanascie","trzynascie","czternascie","pietnascie",
           "szesnascie","siedemnascie","osiemnascie","dziewietnascie"]
dziesiatki=["","dziesiec","dwadziescia","trzydziesci","czterdziesci","piecdziesiat",
            "szescdziesiat","siedemdziesiat","osiemdziesiat","dziewiecdziesiat"]
setki=["","sto","dwiescie","trzysta","czterysta","piecset","szescset","siedemset","osiemset",
       "dziewiecset"]
tysiace=["","tysiac"]

def konwersja(liczba):
    if liczba>0 and liczba<=10:
        temp=int(liczba/1)
        wynik=jednosci[temp]
        return wynik
    elif liczba>10 and liczba <=19:
        temp=int(liczba/1)
        wynik=wyjatkowe[temp-10]
        return wynik
    elif liczba>19 and liczba<=99:
        a=liczba//10 #indeks dziesiatek
        b=liczba%10 #indeks jednosci
        wynik=dziesiatki[a],jednosci[b]
        return wynik
    elif liczba>99 and liczba<1000:
        a=liczba//100 #indeks setek
        temp=liczba%100
        if temp>10 and temp<=19:
            wynik=setki[a]+" "+wyjatkowe[temp-10]
            return wynik
        b=temp//10 #indeks dziesiatek
        c=temp%10 #indeks jednosci
        wynik=setki[a]+" "+dziesiatki[b]+" "+jednosci[c]
        return wynik
    elif liczba>1000 and liczba<=1999:
        a=liczba//1000 #indeks tysiecy
        temp=liczba%1000
        b=temp//100 #indeks setek
        temp2=temp%100
        if temp2>10 and temp2<=19:
            wynik=tysiace[a]+" "+setki[b]+" "+wyjatkowe[temp2-10]
            return wynik
        c=temp2//10 #indeks dziesiatek
        d=temp%10 #indeks jednosci
        wynik=tysiace[a]+" "+setki[b]+" "+dziesiatki[c]+" "+jednosci[d]
        return wynik
    else:
        print("Program nie obsluguje liczb wiekszych niż 1999..")
        

def test():
    assert konwersja(1511) == "tysiac piecset jedenascie","False"
    assert konwersja(698) == "szescset dziewiecdziesiat osiem","False"
  
test()
"""
print("Podaj liczbe dziesietna, a program zamieni ja na wartosc slowna.")
wartosc=int(input("Twoja liczba:"))
konwersja(wartosc)
"""