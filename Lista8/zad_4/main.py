import pesel

try:
    file_location=input("Podaj sciezke do pliku:")
    file = open(file_location,"r",errors='ignore')
    info=open("information.txt","w+")
except:
    print("Problem with reading a file.")
else:
    print("File successfully loaded!")
    content=file.read()
    for i in content.splitlines():
        if pesel.check_control_digit(i):
            info.write("nr %s\ndata urodzenia:%s\tpłeć:%s\n" %(i,pesel.date_birth(i),pesel.sex(i)))
    file.close()
    info.close()