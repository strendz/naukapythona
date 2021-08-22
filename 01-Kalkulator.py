print("Jestem kalkulatorem, pomoge ci obliczyc wszystkie dzialania z (dodawania, odejmowani,a mnozenia lub dzielenia")
print(" ")
print("dodawanie - 1 ")
print("odejmowanie - 2 ")
print("mnozenie - 3 ")
print("dzielenie - 4 ")
print(" ")

dzialanie = input("Podaj jakie dzialanie chcesz wykonac ")
#dzialanie = int(dzialanie)
if dzialanie != "1" and dzialanie != "2" and dzialanie != "3" and dzialanie != "4":
    print("Niewlasciwa komenda! ")
    
    
else:
    pierwszaliczba = input("Podaj pierwsza liczbe ")
    drugaliczba = input("Podaj druga liczbe ")

    pierwszaliczba = int(pierwszaliczba)
    drugaliczba = int(drugaliczba)
    

    if dzialanie == "1":
        print("Oto twoj wynik: " , pierwszaliczba+drugaliczba)
    elif dzialanie == "2":
        print("Oto twoj wynik: " , pierwszaliczba-drugaliczba)
    elif dzialanie == "3":
        print("Oto twoj wynik: " , pierwszaliczba*drugaliczba)
    elif dzialanie == "4":
        if drugaliczba == 0:
            print("Nie dzieli sie przez zero! ")
        else:
                print("Oto twoj wynik: " , pierwszaliczba/drugaliczba)