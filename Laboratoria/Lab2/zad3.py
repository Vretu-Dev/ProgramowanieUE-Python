liczba = int(input("Podaj liczba: "))
licznik = 0

while licznik < liczba:
    licznik += 1

    if licznik % 2 == 0:
        continue

    print(licznik)