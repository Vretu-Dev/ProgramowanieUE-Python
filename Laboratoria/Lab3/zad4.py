import math

print("Podaj zakres liczb")
liczba1 = int(input("Podaj pierwszą: "))
liczba2 = int(input("Podaj drugą: "))

lista = []
wynik = []

for i in range(liczba1, liczba2):
    if i % 2 != 0:
        lista.append(i)
        wynik.append( (i, math.pow(i, 2), round(math.sqrt(i),2) ) )

print("Dla listy:", end=' ')
print(lista)

print("Wynik:", end=' ')
print(wynik)
