
import SzyfrCezara
import os
import re
from pathlib import Path

file_location=input("File location:")

if not os.path.exists(file_location):
    print("The specified path does not exists")
else:
    print("The specified path exists")
    list_files=[]
    list_keys=[]
    for entry in Path(file_location).iterdir():
        list_files.append(entry.name)
    print("List of files:")
    for i in range(len(list_files)):
        print(list_files[i])
        key=re.search('\d',list_files[i])
        list_keys.append(int(key.group()))
    for j in range(len(list_keys)):
        try:
            file = open(file_location+"/"+list_files[j],"r",errors='ignore')
        except:
            print("Problem with reading a file.")
        else:
            print("File successfully loaded!")
            SzyfrCezara.deszyfrowanie(file.read(),list_keys[j])
            file.close()
    