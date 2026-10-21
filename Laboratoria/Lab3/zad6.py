import math

n = int(input("Podaj wymiary macierzy kwadratowej: "))

tablica = []

for i in range(n):
    wiersz = []
    liczba_wiersza = i + 1
    for j in range(n):
        liczba_kolumny = j + 1

        if math.gcd(liczba_wiersza, liczba_kolumny) == 1:
            wiersz.append("+")
        else:
            wiersz.append("-")

    tablica.append(wiersz)

# Numer kolumny
print("   " + " ".join(f"{col:>2}" for col in range(1, n + 1)))

# Numer wiersza + znaki
for i in range(n):
    numer_wiersza = i + 1
    znaki = "  ".join(tablica[i])
    print(f"{numer_wiersza:>2}  {znaki}")


