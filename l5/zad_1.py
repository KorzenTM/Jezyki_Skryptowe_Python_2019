# -*- coding: utf-8 -*-
"""
Created on Fri Nov  8 10:06:50 2019

@author: mateu
"""

#zamiana wartoci słownej na liczbę z zakresu 1-59

liczby={"jeden":1,"dwa":2,"trzy":3,"cztery":4,"piec":5,"szesc":6,"siedem":7,"osiem":8,
        "dziewiec":9,"dziesiec":10,"jedenascie":11,"dwanascie":12,"trzynascie":13,
        "czternascie":14,"pietnascie":15,"szesnascie":16,"siedemnascie":17,
        "osiemnascie":18,"dziewietnascie:":19,"dwadziescia":20,"trzydziesci":30,
        "czterdziesci":40,"piecdziesiat":50}

def konwersja(liczba_slownie):
    wynik=0
    tablica_slow=liczba_slownie.split(" ") #dzielimy string na poszczególne wyrazy
    
    for i in range(len(tablica_slow)):
        temp=liczby[tablica_slow[i]]
        wynik=wynik+temp
        
    return wynik
        
def test():
    assert konwersja("jeden") == 1,"Bład"
    assert konwersja("trzydziesci trzy") == 33,"Błąd"
    assert konwersja("trzynascie") == 13,"Błąd"
         
        
test()   
"""      
print("Podaj liczbę słownie, a program zamieni ją na liczbę dziesietną.")
wartosc=input("Twoja liczba:")
konwersja(wartosc)
"""