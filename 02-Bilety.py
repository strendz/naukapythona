print("Jestem kalkulatorem, pomoge ci policzyć kazde dzialanie (dodawanie, odejmowanie, mnozenie lub dzielenie)")
print(" ")
print("dodawanie - 1")
print("odejmowanie - 2")
print("mnozenie - 3")
print("dzielenie - 4")

dzialanie = input("Napisz ktore dzialanie chcesz wykonac ")
pierwszaliczba = input("Podaj pierwsza liczbe ")
drugaliczba = input("Podaj druga liczbe ")

pierwszaliczba = int(pierwszaliczba)
drugaliczba = int(drugaliczba)

if dzialanie == "1":
    wynik = pierwszaliczba+drugaliczba
elif dzialanie == "2":
    wynik = pierwszaliczba-drugaliczba
elif dzialanie == "3":
    wynik = pierwszaliczba*drugaliczba
elif dzialanie == "4":
    if drugaliczba == 0:
        print("Nie dzieli sie przez zero! ")

    else:
        wynik = pierwszaliczba/drugaliczba
        print("Oto twoj wynik: " , wynik)
