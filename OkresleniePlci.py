from time import sleep

print("Jestem programem okreslajacy plec ")
print("Musisz jedynie podac swoje imie a ja sproboje okreslic twoja plec ")
print()
sleep(2)
name = input("Twoje imie: ")

if name[-1] != "a":
    print("Jestes mezczyzna ")
if name[-1] == "a":
    print("Jestes kobieta")