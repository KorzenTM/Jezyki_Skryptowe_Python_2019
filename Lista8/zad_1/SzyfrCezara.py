import os
from datetime import datetime

now=datetime.now()
def write_file(napis_2,key):
    file_location=input("Gdzie chcesz zapisac plik?:")
    if not os.path.exists(file_location):
        try:
            os.makedirs(file_location)
        except:
            print("The problem with creating a folder.")
        else:
            print("Folder successfully created!")
    try:
        new_file=open(file_location+"/plik_zaszyfrowany%d_%s%s%s.txt" %(key,now.strftime("%Y"),now.strftime("%m"),now.strftime("%d")),"w")
    except:
        print("Problem with creating file.")
    else:
        print("File successfully created")
        try:
            new_file.write(napis_2)
        except:
            print("Problem with saving data to a file.")
        else:
            print("The data has been saved.")
    new_file.close()
    

def szyfrowanie(napis,key):
    napis_2="" #zaszyfrowany napis
    for i in range(len(napis)):
        if napis[i].isalpha()==1 and napis[i].islower()==1:
            if ord(napis[i])>122-key: #w przypadku wyjscia poza alfabet cofamy sie do poczatku(male litery)
                napis_2+=chr(ord(napis[i])+key-26)
            else:
                napis_2+=chr(ord(napis[i])+key) 
        elif napis[i].isalpha()==1 and napis[i].isupper()==1:
            if ord(napis[i])>90-key:
                napis_2+=chr(ord(napis[i])+key-26)#w przypadku wyjscia poza alfabet cofamy sie do poczatku(duze litery)
            else:
                napis_2+=chr(ord(napis[i])+key)
        else: #jesli znak nie jest litera pozostawiamy bez zmian
            napis_2+=napis[i]
    write_file(napis_2,key)       
    return

