import random

n = int(input("Podaj wymiary macierzy kwadratowej: "))

print("Podaj zakres liczb")
liczba1 = int(input("Podaj pierwszą: "))
liczba2 = int(input("Podaj drugą: "))

if liczba1 > liczba2:
    temp = liczba1
    liczba1 = liczba2
    liczba2 = temp

matrix = [[random.randint(liczba1, liczba2) for _ in range(n)] for _ in range(n)]

sumaLewejPrzekatnej = 0
sumaPrawejPrzekatnej = 0
sumaNieparzystychIndeks = 0

for i in range(n):
    for j in range(n):
        print(f"{matrix[i][j]:2}", end=" ")

        # Lewa przekątna
        if i == j:
            sumaLewejPrzekatnej += matrix[i][j]
        # Prawa przekątna
        if i + j == n - 1:
            sumaPrawejPrzekatnej += matrix[i][j]

        # Nieparzyste indeksy
        if i % 2 != 0 and j % 2 != 0:
            sumaNieparzystychIndeks += matrix[i][j]
    print()

print(f"Suma lewej przekątnej {sumaLewejPrzekatnej}")
print(f"Suma prawej przekątnej: {sumaPrawejPrzekatnej}")
print(f"Suma nieparzystych indeksów przekątnej: {sumaNieparzystychIndeks}")

odwrotna = [row[::-1] for row in matrix][::-1]

print(matrix)
print(odwrotna)