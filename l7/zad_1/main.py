#Fibonacci series through iteration and recursion
import time

def fibo_rec(N):
    if N==0:
        return 0
    if N==1:
        return 1
    else:
        return fibo_rec(N-1)+fibo_rec(N-2)

def fibo_iter(N):
    a=0 #F0
    b=1 #F1
    temp=0 #temporary sum
    for i in range(N-1):
        temp=a+b
        a=b
        b=temp
    return temp


N=int(input("Podaj N:"))
start=time.time()
print("Recurencion method:",fibo_rec(N))
end = time.time()
print("Time:",end-start)
start=time.time()
print("Iteration method:",fibo_iter(N))
end=time.time()
print("Time:",end-start)