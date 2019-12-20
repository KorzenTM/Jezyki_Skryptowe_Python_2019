import itertools
class lista:
    def __init__(self,lista):
       self.lista= lista
    def substratum(self):
        new_list=[]
        for n in range(len(self.lista)+1):
            res=itertools.combinations(self.lista,n)
            new_list.append(list(res))
        return new_list
    
example=[1,2,3]
sub=lista(example)
print(sub.substratum())

        
     