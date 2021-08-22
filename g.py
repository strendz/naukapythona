from time import sleep
from random import randint
odp = 10000
proba = 0
print("Jestem programem ktory losuje liczbe od 1 - 100")
print("Twoim zadaniem jest odgadniecie jej i wygranie ")
print()
sleep(2)
print("Losuje liczbe",end="")
for:
    sleep(0.5)
    print(".",end="")
print("Liczba zostala wylosowana! ")
print()
sleep(2)
los = randint(1,100)

while odp != los:
    odp = int(input("Twoja liczba: "))
    proba = proba + 1
    if odp > los:
        print("Za duza! ")
    elif odp < los:
        print("Za mala! ")

print("Brawo wygral*s! ")
print("Udalo ci sie w",proba,"probach! ")