liczba = input("Podaj liczbę: ")

suma = 0
parzyste = []
nieparzyste = []

for znak in liczba:
    if not znak.isdigit():
        continue
    cyfra = int(znak)
    suma += cyfra
    if cyfra % 2 == 0:
        parzyste.append(cyfra)
    else:
        nieparzyste.append(cyfra)

sredniaParzyste = sum(parzyste) / len(parzyste) if parzyste else "brak" # if warunek ? true : false
sredniaNieparzyste = sum(nieparzyste) / len(nieparzyste) if nieparzyste else "brak"

print("=" * 50)
print(f"Suma cyfr liczby {suma}")
print(f"Średnia arytmetyczna liczb parzystych {sredniaParzyste}")
print(f"Średnia arytmetyczna liczb nieparzystych {sredniaNieparzyste}")
print("=" * 50)