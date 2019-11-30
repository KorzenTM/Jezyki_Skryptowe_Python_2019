# -*- coding: utf-8 -*-
"""
Created on Wed Oct 30 10:58:50 2019

@author: mateu
"""
import colorsys

print("Podaj wartosc R:")
R=int(input())
print("Podaj wartosc G:")
G=int(input())
print("Podaj wartosc B:")
B=int(input())

R=R/255
G=G/255
B=B/255
lista=colorsys.rgb_to_hsv(R,G,B)
print("H\tS\tV")
print(lista[0]*360,"",lista[1]*100,"",lista[2]*100)