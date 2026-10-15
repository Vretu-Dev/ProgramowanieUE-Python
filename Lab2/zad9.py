from copy import deepcopy

liczba = int(input("Podaj liczba: "))

isDoskonala = True
isPierwsza = True
dzielniki = []

for i in range(1, liczba + 1):
    if liczba % i == 0:
        dzielniki.append(i)

if len(dzielniki) != 2:
    isPierwsza = False

doskonale = deepcopy(dzielniki)
doskonale.pop()

sumaDoskonale = sum(doskonale)

if sumaDoskonale != liczba:
    isDoskonala = False

print(f"Dzielniki liczby {liczba} to {dzielniki}\n"
      f"Czy pierwsza: {isPierwsza}\n"
      f"Czy doskonała: {isDoskonala}")
