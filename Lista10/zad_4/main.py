import xml.etree.ElementTree as ET

class exchange_rate:
    def __init__(self, file_location,choice):
        self.file_location=file_location
        self.choice=choice
    def exchange_table(self):
        course={}
        tree=ET.parse(self.file_location)
        root=tree.getroot()
        for pozycja in root.findall('pozycja'):
            kod=pozycja.find('kod_waluty').text
            kurs=pozycja.find('kurs_sredni').text
            course[kod]=float(kurs)
        if self.choice==1:
            print("|{:35s}|{:11s}|{:10s}|{:3s}" .format("Nazwa waluty","Przelicznik","Kod waluty","Kurs sredni"))
            for pozycja in root.findall('pozycja'):
                nazwa=pozycja.find('nazwa_waluty').text
                przelicznik=pozycja.find('przelicznik').text
                kod=pozycja.find('kod_waluty').text
                kurs=pozycja.find('kurs_sredni').text
                print("|{:35s}|{:11s}|{:10s}|{:3s}" .format(nazwa,przelicznik,kod,kurs))
            return "Stan:2019-12-20"
        elif self.choice==2:
            PLN=float(input("Kwota w PLN:"))
            currency=input("Chcesz otrzymac(uzyj kodu waluty):")
            print("Aktualny kurs:",course[currency])
            print("Twoja kwota w wybranej walucie:")
            return PLN/course[currency]
        elif self.choice==3:
            currency_1=input("Jaka walute wymieniasz(uzyj kody):")
            amount=float(input("Twoja kwota:"))
            currency_2=input("Na jaka walute chcesz wymienic(uzyj kodu):")
            print("Twoja kwota w wybranej walucie:")
            return (amount*course[currency_1])/course[currency_2]
        else:
            print("Niepoprawny wybor. Zamykanie programu...")   
    
        
path=input("Lokalizacja pliku z kursami:") 
print("|PRZELICZNIK WALUT|")
print("1. Lista dostepnych kursow.")
print("2. Konwersja PLN <-> wybrana waluta")
print("3. Konwersja wybrana waluta <-> wybrana waluta")
choice=int(input("Wybor:"))      
kursy=exchange_rate(path,choice)
print(kursy.exchange_table())
