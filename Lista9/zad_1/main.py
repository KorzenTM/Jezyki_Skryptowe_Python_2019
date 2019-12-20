# -*- coding: utf-8 -*-

#a system of linear equations
import numpy as np

A=np.array([[1,2,3,-2,-1],[3,5,5,-3,-9],[2,3,2,0,-8],[2,6,7,-5,1],[1,2,6,-4,-10]])
B=np.array([6,2,-5,17,12]).T
res=np.linalg.solve(A,B)
print("x=",res[0],"\ny:",res[1],"\nz:",res[2],"\nt:",res[3],"\nu:",res[4])