# -*- coding: utf-8 -*-
"""
Created on Wed Oct 30 10:41:59 2019

@author: mateu
"""

import itertools
lista=[21,18,19]
 
perm=itertools.permutations(lista)

for i in list(perm):
    print(i)