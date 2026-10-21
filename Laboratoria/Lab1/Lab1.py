from copy import deepcopy

print("Hello World")

'''stan_konta = input("Podaj stan konta: ")
stan_konta = int(stan_konta)
stan_konta += 500*2

print(stan_konta)'''


temperatura = -5

if temperatura > 10:
    print("Wychodzimy")
else:
    print("Nie wychodzimy")

for i in range(10):
    print("Iteracja:", i)

oceny = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Przestarzałe podejście
for i in range(len(oceny)):
    print(oceny[i], end=" ")

print()

# Foreach z C#?
for ocena in oceny:
    print(ocena, end=" ")

print()

# Sposób 1
for i, ocena in enumerate(oceny):
    if i % 2 == 0 and ocena > 3:
        print(ocena, end=" ")

print()

# Sposób 2
for ocena in oceny:
    ocena += 1
    print(ocena, end=" ")

#
oceny.append(10) # Dodaje na koniec
oceny.extend([11, 12, 13]) # Dodaje na koniec kilka
oceny.insert(1, 14) # Wstawia na podany indeks. 14 wyląduje na index 1
oceny.remove(6) # Usuwa element tablicy który jest 6 (NIE INDEX)
oceny.pop() # Usuwa ostatni element w tablicy
oceny.sort() # Sortuje tablice 1 Sposób
oceny = sorted(oceny) # Sortuje tablice 2 Sposób
oceny = sorted(oceny, reverse=True) # Sortuje na malejąco
print()

for ocena in oceny:
    print(ocena, end=" ")

print()

if 6 in oceny:
    print(oceny.index(6)) # Pokaże index na którym znajduje sie 6 w tablicy


## 2 wymiarowe

oceny_all = [[1,2,3],[4,5,6],[7,8,9]]

print(oceny_all[0][1])

for student in oceny_all:
    for ocena in student:
        print(ocena, end=" ")
    print()

oceny_2 = deepcopy(oceny_all)

oceny_2[0][0] = 99

for student in oceny_2:
    for ocena in student:
        print(ocena, end=" ")
    print()


oceny_3 = {1,1,1,2,2,2,3,3,3}

for ocena in oceny_3:
    print(ocena, end=" ")

oceny = set(oceny) # Unikalne Wartości

print(oceny)


oceny_kuba = [5, 4, 3, 5, 5, 5]
oceny_marek = [1, 2, 3, 1, 1, 1]

set_kuba = set(oceny_marek)
set_marek = set(oceny_kuba)

print(set_kuba.intersection(set_marek)) # Część wspólna
print(set_kuba.difference(set_marek))

oceny = list(set(oceny))
print(oceny)

# Słowniki
oceny_slownik = {}
oceny_slownik["jakub"] = [5, 4, 3, 5, 5, 5]
oceny_slownik["marek"] = [1, 2, 3, 1, 1, 1]

print(oceny_slownik["jakub"])

for k,v in oceny_slownik.items():
    print(k, v)

## String

imie = "Wojtek"
imie = imie.lower()


print(imie[0])

imie = imie.replace("k", "K")

print(imie)

new_string = imie + " " + imie
print(new_string)

'''imie = imie.split("j")
print(imie)'''

## F String działa jak $ w C#
f_string = f"{imie} jest kozakiem"
print(f_string)


print(f_string[-1]) ## ostatni element od końca
print(f_string[3:]) ## wypisuje od 3 elementu do końca tablicy
print(f_string[3:5]) ## wypisuje od 3 elementu do 5

## Pliki
lines = []
with open("plik.txt") as f:
    for line in f:
        lines.append(line.strip()) # strip usuwa białe znaki
    print(lines)


## Funkcje

silniaLinia = []
with open("silniaplik.txt") as f:
    for line in f:
        silniaLinia.append(int(line.strip()))

def silnia(n):
    res = 1
    for x in range(1, n+1):
        res = res * x
    return res

print(silnia(5))

for number in silniaLinia:
    print(silnia(number))

## Wbudowane Funkcje
from math import gcd

print(gcd(24,46))