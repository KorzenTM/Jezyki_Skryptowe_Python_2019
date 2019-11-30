#sorting by inserting
import random
import time

def sort_insert(data):
    for i in range(1,len(data)):
        j=0
        key=data[i]
        while key>data[j] and j<i:
            j+=1
        data.insert(j, key)
        del data[i+1]
    return data


def random_list(n):
    unsorted_list=[]
    for i in range(n):
        unsorted_list.append(random.randint(0,20))
    return sort_insert(unsorted_list)

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
