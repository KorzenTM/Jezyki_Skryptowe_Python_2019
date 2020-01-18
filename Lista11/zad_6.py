class CiagArytmetyczny:
    def __init__(self,a1,r,n):
        self.a1=a1
        self.r=r
        self.n=n
        self.start=0
        self.file=open('ciag.txt','w')
    def __iter__(self):
        return self
    def __next__(self):
        if self.start>=self.n:
            self.file.close()
            raise StopIteration
        else:
            self.start+=1
            val=self.a1+(self.start-1)*self.r
            self.file.write(str(val)+"\n")
            return val
    def __len__(self):
        return self.n
        
res=CiagArytmetyczny(5,12,10)
for i in res:
    print(i)