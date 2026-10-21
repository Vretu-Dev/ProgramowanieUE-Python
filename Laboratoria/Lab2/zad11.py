# Zadanie 11: Rozwiązywanie układu 2 równań liniowych metodą eliminacji Gaussa
# Układ postaci:
# a1 * x + b1 * y = c1
# a2 * x + b2 * y = c2

def pobierz_wspolczynnik(nazwa):
    while True:
        try:
            return float(input(f"Podaj współczynnik {nazwa}: "))
        except ValueError:
            print("Błąd: wprowadź poprawną liczbę!")

print("=" * 55)
print("  ROZWIĄZYWANIE UKŁADU RÓWNAŃ METODĄ ELIMINACJI GAUSSA")
print("          a1*x + b1*y = c1")
print("          a2*x + b2*y = c2")
print("=" * 55)

print("\n--- Równanie 1 ---")
a1 = pobierz_wspolczynnik("a1")
b1 = pobierz_wspolczynnik("b1")
c1 = pobierz_wspolczynnik("c1")

print("\n--- Równanie 2 ---")
a2 = pobierz_wspolczynnik("a2")
b2 = pobierz_wspolczynnik("b2")
c2 = pobierz_wspolczynnik("c2")

# Tworzymy macierz rozszerzoną układu [A|B]
# Wiersz 1: [a1, b1, c1]
# Wiersz 2: [a2, b2, c2]
R1 = [a1, b1, c1]
R2 = [a2, b2, c2]

print("\nPostać początkowa macierzy rozszerzonej [A | B]:")
print(f"[{R1[0]:8.2f} {R1[1]:8.2f} | {R1[2]:8.2f}]")
print(f"[{R2[0]:8.2f} {R2[1]:8.2f} | {R2[2]:8.2f}]")

EPSILON = 1e-9

# 1. Wybór elementu podstawowego (pivoting) - jeśli w pierwszym wierszu a1 jest zerem, zamieniamy wiersze
if abs(R1[0]) < EPSILON and abs(R2[0]) >= EPSILON:
    print("\n[Operacja] Zamiana wiersza 1 z wierszem 2 (aby uniknąć zera na przekątnej)")
    R1, R2 = R2, R1

# 2. Eliminacja Gaussa
if abs(R1[0]) < EPSILON and abs(R2[0]) < EPSILON:
    # Współczynniki przy x w obu równaniach to 0
    if abs(R1[1]) < EPSILON and abs(R2[1]) < EPSILON:
        if abs(R1[2]) < EPSILON and abs(R2[2]) < EPSILON:
            print("\nWynik: Układ tożsamościowy (nieoznaczony) - nieskończenie wiele rozwiązań.")
        else:
            print("\nWynik: Układ sprzeczny - brak rozwiązań.")
    else:
        print("\nZmienna x nie występuje w układzie. Równania zawierają tylko y.")
        # Sprawdzamy wyznaczenie y
        y1 = R1[2] / R1[1] if abs(R1[1]) >= EPSILON else None
        y2 = R2[2] / R2[1] if abs(R2[1]) >= EPSILON else None
        if y1 is not None and y2 is not None:
            if abs(y1 - y2) < EPSILON:
                print(f"Rozwiązanie: y = {y1:.2f}, x należy do zbioru liczb rzeczywistych.")
            else:
                print("Wynik: Układ sprzeczny - brak rozwiązań.")
        elif y1 is not None:
            print(f"Rozwiązanie: y = {y1:.2f}, x należy do zbioru liczb rzeczywistych.")
        else:
            print(f"Rozwiązanie: y = {y2:.2f}, x należy do zbioru liczb rzeczywistych.")
else:
    # Wyzerowanie współczynnika przy x w drugim wierszu
    wspolczynnik_m = R2[0] / R1[0]
    print(f"\n[Operacja] Wiersz 2 = Wiersz 2 - ({wspolczynnik_m:.2f}) * Wiersz 1")

    R2[0] = 0.0
    R2[1] = R2[1] - wspolczynnik_m * R1[1]
    R2[2] = R2[2] - wspolczynnik_m * R1[2]

    print("\nMacierz po eliminacji (postać schodkowa):")
    print(f"[{R1[0]:8.2f} {R1[1]:8.2f} | {R1[2]:8.2f}]")
    print(f"[{R2[0]:8.2f} {R2[1]:8.2f} | {R2[2]:8.2f}]")

    # 3. Analiza rozwiązań i postępowanie wsteczne (back-substitution)
    if abs(R2[1]) < EPSILON:
        if abs(R2[2]) < EPSILON:
            print("\nWynik: Układ nieoznaczony - nieskończenie wiele rozwiązań (zależnych od jednego parametru).")
        else:
            print("\nWynik: Układ sprzeczny (0 = const != 0) - brak rozwiązań.")
    else:
        # Dokładnie jedno rozwiązanie
        y = R2[2] / R2[1]
        x = (R1[2] - R1[1] * y) / R1[0]
        print("\n" + "=" * 35)
        print("  UKŁAD OZNACZONY (JEDNO ROZWIĄZANIE)")
        print(f"  x = {x:.4f}")
        print(f"  y = {y:.4f}")
        print("=" * 35)
