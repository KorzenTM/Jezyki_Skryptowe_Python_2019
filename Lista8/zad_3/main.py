import pesel
import os

f = open("PESEL.TXT","w+")
for i in range(10):
    f.write(pesel.generate()+"\n")
f.close()