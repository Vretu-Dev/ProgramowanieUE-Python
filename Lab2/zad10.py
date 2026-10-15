
def czy_pierwsza(liczba):
    if liczba < 2:
        return False

    for d in range(2, int(liczba ** 0.5) + 1):
        if liczba % d == 0:
            return False
    return True

while True:
    try:
        n = int(input("Podaj liczbę całkowitą n (n > 1): "))
        if n > 1:
            break
        print("Liczba musi być większa niż 1! Spróbuj ponownie.")
    except ValueError:
        print("Nieprawidłowa wartość! Wprowadź liczbę całkowitą.")

if czy_pierwsza(n):
    print(f"\nLiczba {n} JEST liczbą pierwszą.")
else:
    print(f"\nLiczba {n} NIE JEST liczbą pierwszą.")

pierwsze_w_zakresie = [x for x in range(2, n + 1) if czy_pierwsza(x)]

print(f"\nLiczby pierwsze w zakresie od 1 do {n} (łącznie {len(pierwsze_w_zakresie)}):")
print(pierwsze_w_zakresie)
