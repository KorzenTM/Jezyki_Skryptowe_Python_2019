# -*- coding: utf-8 -*-
#statistic calculation
import numpy as np
number=int(input("How much measurement data do you want to enter?:"))
data=[]
print("Enter your data:")
for i in range(number):
    records=float(input())
    data.append(records)
print("Your data:")
print(data)
print("Mean:",np.mean(data))
print("Standard deviation:",np.std(data))
print("Variance:",np.var(data))


