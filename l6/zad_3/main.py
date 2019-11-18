
N=int(input("Podaj n-ty "))

i=0

while i<N:
    if i==0:
        series=[1]
    else:
        cnt=1
        tmpseries=[]
        for j in range(1,len(series)):
            if series[j] == series[j-1]:
                cnt+=1
            else:
                tmpseries+=[cnt,series[j-1]]
                cnt=1
        tmpseries+=[cnt,series[len(series)-1]]
        series=tmpseries
    i+=1
    print("Wyraz",i,"-",series)



