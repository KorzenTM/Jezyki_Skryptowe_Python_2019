#bubble sorting
import random
import time

def bubble_sort(data):
    for i in range(len(data)):
        j=len(data)-1
        while j>i:
            if data[j]<data[j-1]:
                tmp=data[j]
                data[j]=data[j-1]
                data[j-1]=tmp
            j-=1
           
    return data
  
def random_list(n):
    unsorted_list=[]
    for i in range(n):
        unsorted_list.append(random.randint(0,20))
    return bubble_sort(unsorted_list)

start=time.time()
print(random_list(100))
end=time.time()
print("Time:",end-start,"[s]")

start=time.time()
print(random_list(200))
end=time.time()
print("Time:",end-start,"[s]")

start=time.time()
print(random_list(300))
end=time.time()
print("Time:",end-start,"[s]")