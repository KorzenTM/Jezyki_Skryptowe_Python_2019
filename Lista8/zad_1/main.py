# -*- coding: utf-8 -*-
"""
Created on Mon Nov 18 12:35:04 2019

@author: mateu
"""
import SzyfrCezara
try:
    file_location=input("Podaj sciezke do pliku:")
    file = open(file_location,"r",errors='ignore')
except:
    print("Problem with reading a file.")
else:
    print("File successfully loaded!")
    key=int(input("Podaj przesuniecie(1-10):"))
    SzyfrCezara.szyfrowanie(file.read(),key)
    file.close()


 