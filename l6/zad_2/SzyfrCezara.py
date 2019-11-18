# -*- coding: utf-8 -*-
"""
Created on Mon Nov 18 12:36:59 2019

@author: mateu
"""

key=3

def szyfrowanie(napis):
    napis_2="" #zaszyfrowany napis
    for i in range(len(napis)):
        if napis[i].isalpha()==1 and napis[i].islower()==1:
            if ord(napis[i])>122-key: #w przypadku wyjscia poza alfabet cofamy sie do poczatku(male litery)
                napis_2+=chr(ord(napis[i])+key-26)
            else:
                napis_2+=chr(ord(napis[i])+key) 
        elif napis[i].isalpha()==1 and napis[i].isupper()==1:
            if ord(napis[i])>90-key:
                napis_2+=chr(ord(napis[i])+key-26)#w przypadku wyjscia poza alfabet cofamy sie do poczatku(duze litery)
            else:
                napis_2+=chr(ord(napis[i])+key)
        else: #jesli znak nie jest litera pozostawiamy bez zmian
            napis_2+=napis[i]
            
    print("Zaszyfrowany napis:",napis_2)
    return


def deszyfrowanie(napis):
    napis_2="" #odszyfrowany napis
    for i in range(len(napis)):
        if napis[i].isalpha()==1 and napis[i].islower()==1:
            if ord(napis[i])-key<97: #w przypadku wyjscia poza alfabet cofamy sie do poczatku(male litery)
                napis_2+=chr(ord(napis[i])-key+26)
            else:
                napis_2+=chr(ord(napis[i])-key) 
        elif napis[i].isalpha()==1 and napis[i].isupper()==1:
            if ord(napis[i])-key<65:
                napis_2+=chr(ord(napis[i])-key+26)#w przypadku wyjscia poza alfabet cofamy sie do poczatku(duze litery)
            else:
                napis_2+=chr(ord(napis[i])-key)
        else: #jesli znak nie jest litera pozostawiamy bez zmian
            napis_2+=napis[i]
            
    print("Zaszyfrowany napis:",napis_2)
    return
