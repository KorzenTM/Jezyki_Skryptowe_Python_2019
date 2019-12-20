# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt

labels=["Java","C","Python","C++","C#","Visual Basic .NET","JavaScript","PHP","SQL","Swift"]
values=[17.253,16.086,10.308,6.196,4.801,4.743,2.090,2.048,1.843,1.490]

plt.bar(labels,values)
plt.xticks(rotation=30)
plt.title("Popularity of programming languages")
plt.ylabel("Ratings[%]")
plt.xlabel("Programming Language")
plt.show()