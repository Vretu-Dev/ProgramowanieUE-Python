while True:
    cenaTowaru = float(input("Podaj cena towaru: "))

    if cenaTowaru < 100 or cenaTowaru > 10000:
        print("Nieprawidłowa cena towaru zakres (100zł - 10.000zł)")
        continue
    else:
        break

while True:
    liczbaRat = int(input("Podaj liczbe rat: "))
    oprocentowanie = 0

    if liczbaRat >= 6 and liczbaRat <= 12:
        oprocentowanie = 0.025
        break
    if liczbaRat >= 13 and liczbaRat <= 24:
        oprocentowanie = 0.05
        break
    if liczbaRat >= 25 and liczbaRat <= 48:
        oprocentowanie = 0.1
        break
    else:
        print("Nieprawidłowa zakres rat (6 - 48)")
        continue

odsetki = cenaTowaru * oprocentowanie
calkowitaCenaTowaru = cenaTowaru + odsetki
odsetkiMiesiac = calkowitaCenaTowaru / liczbaRat

# 4. Raport podsumowujący
print("\n" + "=" * 44)
print("         RAPORT SPRZEDAŻY RATALNEJ          ")
print("=" * 44)
print(f" Cena towaru:             {cenaTowaru:>10.2f} zł")
print(f" Liczba rat:              {liczbaRat:>10} mies.")
print(f" Stopa oprocentowania:    {oprocentowanie * 100:>10.1f} %")
print("-" * 44)
print(f" Kwota odsetek:           {odsetki:>10.2f} zł")
print(f" Łącznie do zapłaty:      {calkowitaCenaTowaru:>10.2f} zł")
print("=" * 44)
print(f" WYSOKOŚĆ MIESIĘCZNEJ RATY:{odsetkiMiesiac:>9.2f} zł")
print("=" * 44)