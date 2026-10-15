import random

print(f"Gra 'Za dużo, za mało'\n"
      f"Podaj poziom trudności:\n"
      f"Easy (1) - Przedział 1-50 | 10 Szans\n"
      f"Medium (2) - Przedział 1-100 | 15 Szans\n"
      f"Hard (3) - Przedział 1-200 | 20 Szans")

poziom = 0
szansa = 0

while poziom not in (1, 2 ,3):
    poziom = int(input("Podaj poziom: "))

    if poziom == 1:
        losowa = random.randint(1, 50)
        szansa = 10
    elif poziom == 2:
        losowa = random.randint(1, 100)
        szansa = 15
    elif poziom == 3:
        losowa = random.randint(1, 200)
        szansa = 20

while szansa > 0:
    liczba = int(input(f"(Pozostałe szanse) {szansa}\nPodaj liczbę: "))
    szansa -= 1

    if losowa == liczba:
        print(f"Wygrałeś")
        break
    if losowa > liczba:
        print(f"Wylosowana liczba jest większa niż podana")
    else:
        print(f"Wylosowana liczba jest mniejsza niż podana")

else:
    print(f"Przegrałeś")