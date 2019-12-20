import random

class substratum:
    def __init__(self, n):
        self.n=n
    def sum_of_elements(self):
        print(self.n)
        main_list=[]
        i=3
        while i<=self.n:
            sub_list=[]
            for j in range(3):
                sub_list.append(round(random.uniform(-1000.0,1000.0),2))
            if sub_list[0]+sub_list[1]+sub_list[2]==0:
                main_list.append(sub_list)
                i+=3
            else:
                continue
        return main_list
     
n=12
sub=substratum(n)
print(sub.sum_of_elements())
        