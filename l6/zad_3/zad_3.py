

N=int(input("Podaj n-ty "))

i=0

while i<N:
    if i==0:
        lookandsay=[1] #głowna lista z elementami ciągu
    else:
        counter=1
        tmplas=[] #tymczasowa lista z wartościami ciągu
        for j in range(1,len(lookandsay)):
            if lookandsay[j] == lookandsay[j-1]: #jeśli mamy dwie takie same liczby to ustawiamy zmienna na 2
                counter+=1
            else: # w innym wypadku dodajemy
                tmplas+=[counter,lookandsay[j-1]]
                counter=1 #resetujemy licznik
        tmplas+=[counter,lookandsay[len(lookandsay)-1]] #w przypadku dwóch takich samych liczb dodajemy licznik i element wcześniejszy
        lookandsay=tmplas
    i+=1
    print("Wyraz",i,"-",lookandsay)