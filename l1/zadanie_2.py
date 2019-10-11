# -*- coding: utf-8 -*-
"""
Created on Wed Oct  9 08:17:47 2019

@author: mateu
"""
#obliczanie pola trojkata z wykorzystaniem wzoru
import math

a=3
b=4
angle=47
#zamiana stopni na radiany
rad=(angle*(2*math.pi))/360
#obliczenie pola
pole=(a*b*math.sin(rad))/2
print("Pole trojkata wynosi:",pole)
