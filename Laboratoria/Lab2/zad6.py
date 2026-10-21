tab = []

while True:
    liczba = int(input("Podaj liczbę: "))
    if liczba == 0:
        break
    tab.append(liczba)

suma = max(tab) + min(tab)
srednia = suma / 2

print("=" * 50)
print(f"Suma największej oraz najmniejszej podanej liczby: {suma}")
print("-" * 50)
print(f"Średnia arytmetyczna największej oraz najmniejszej podanej liczby: {srednia}")
print("-" * 50)
print(f"Wszystkie wprowadzone liczby {tab}")
print("=" * 50)