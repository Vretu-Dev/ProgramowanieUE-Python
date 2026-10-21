tab = []

while True:
    liczba = int(input("Podaj liczbę: "))
    if liczba == 0:
        break
    tab.append(liczba)

print(f"Suma wszystkich podanych liczb wynosi {sum(tab)}")