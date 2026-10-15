# Zadanie 12: Algorytm Euklidesa oraz Rozszerzony Algorytm Euklidesa (Tożsamość Bézouta)
# Szukamy NWD(a, b) oraz współczynników całkowitych x, y takich, że:
# a * x + b * y = NWD(a, b)

def pobierz_liczbe(etykieta):
    while True:
        try:
            wartosc = int(input(f"Podaj {etykieta} (liczbę całkowitą dodatnią): "))
            if wartosc > 0:
                return wartosc
            print("Liczba musi być większa od zera!")
        except ValueError:
            print("Wprowadź poprawną liczbę całkowitą!")

print("=" * 65)
print("      ALGORYTM EUKLIDESA I ROZSZERZONY ALGORYTM EUKLIDESA")
print("          Wyznaczanie NWD(a, b) oraz tożsamości Bézouta:")
print("                     a * x + b * y = NWD(a, b)")
print("=" * 65)

a = pobierz_liczbe("liczbę a")
b = pobierz_liczbe("liczbę b")

# 1. Klasyczny algorytm Euklidesa z pełnym przebiegiem
print("\n" + "-" * 65)
print(" CZĘŚĆ 1: KLASYCZNY ALGORYTM EUKLIDESA (Kolejne dzielenia z resztą)")
print("-" * 65)

temp_a, temp_b = a, b
krok = 1

while temp_b != 0:
    q = temp_a // temp_b
    r = temp_a % temp_b
    print(f"Krok {krok:2d}:  {temp_a:6d} = {q:4d} * {temp_b:6d} + {r:6d}   (reszta = {r})")
    temp_a, temp_b = temp_b, r
    krok += 1

nwd = temp_a
print(f"\n=> Największy Wspólny Dzielnik: NWD({a}, {b}) = {nwd}")

# 2. Rozszerzony algorytm Euklidesa (tabelaryczny)
print("\n" + "-" * 65)
print(" CZĘŚĆ 2: ROZSZERZONY ALGORYTM EUKLIDESA (Współczynniki Bézouta)")
print(" Wyznaczamy ciągi r, x, y takie, że w każdym kroku: r_i = x_i * a + y_i * b")
print("-" * 65)

# Stan początkowy:
# r0 = a, x0 = 1, y0 = 0  (bo a = 1*a + 0*b)
# r1 = b, x1 = 0, y1 = 1  (bo b = 0*a + 1*b)
r_prev, r_curr = a, b
x_prev, x_curr = 1, 0
y_prev, y_curr = 0, 1

print(f"{'Krok':^6} | {'Iloraz q':^10} | {'Reszta r':^10} | {'x':^10} | {'y':^10} | {'Równanie: r = x*a + y*b'}")
print("-" * 75)
print(f"{'Start':^6} | {'-':^10} | {r_prev:^10} | {x_prev:^10} | {y_prev:^10} | {r_prev} = ({x_prev})*{a} + ({y_prev})*{b}")
print(f"{'Start':^6} | {'-':^10} | {r_curr:^10} | {x_curr:^10} | {y_curr:^10} | {r_curr} = ({x_curr})*{a} + ({y_curr})*{b}")

krok = 1
while r_curr != 0:
    q = r_prev // r_curr
    r_next = r_prev - q * r_curr
    x_next = x_prev - q * x_curr
    y_next = y_prev - q * y_curr

    print(f"{krok:^6} | {q:^10} | {r_next:^10} | {x_next:^10} | {y_next:^10} | {r_next} = ({x_next})*{a} + ({y_next})*{b}")

    r_prev, r_curr = r_curr, r_next
    x_prev, x_curr = x_curr, x_next
    y_prev, y_curr = y_curr, y_next
    krok += 1

x, y = x_prev, y_prev

print("\n" + "=" * 65)
print(" PODSUMOWANIE I WERYFIKACJA WYNIKÓW:")
print("=" * 65)
print(f" NWD({a}, {b}) = {nwd}")
print(f" Współczynniki Bézouta: x = {x}, y = {y}")
print(f" Równanie Bézouta:      {a} * ({x}) + {b} * ({y}) = {a * x + b * y}")
print(f" Zgodność z NWD:        {a * x + b * y} == {nwd} -> {a * x + b * y == nwd}")
print("=" * 65)
