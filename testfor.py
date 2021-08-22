wynik = 0
liczba = 0
liczba = int(liczba)

print("end - jesli chcesz zakonczyc ")
while True:
    liczba = input("Podaj liczbe ")
    print(liczba+liczba)
    if liczba == "end":
        break
    liczba = int(liczba)
    wynik = liczba + wynik
    
print("Wynik: ",wynik)