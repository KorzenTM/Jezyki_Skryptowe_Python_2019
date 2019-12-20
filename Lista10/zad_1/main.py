import numpy as np
import math

class Kolo:
    def __init__(self, r):
        self.r = r
    def circuit(self):
        res = math.pi*self.r**2
        return res
    def field(self):
        res = 2*math.pi*self.r
        return res


kolo=Kolo(20)
print("Circuit:",kolo.circuit())
print("Field:",kolo.field())