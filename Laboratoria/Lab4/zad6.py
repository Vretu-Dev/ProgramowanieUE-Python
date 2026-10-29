import random

def program_fiszki():
    fiszki = {}

    print("=== ETAP 1: DODAWANIE SŁÓWEK ===")
    print("Wpisz 'stop' jako słowo, aby zakończyć wprowadzanie.\n")

    while True:
        slowo = input("Podaj słowo (język obcy): ").strip()
        if slowo.lower() == "stop":
            break

        if not slowo:
            print("Słowo nie może być puste.")
            continue

        if slowo in fiszki:
            print(f"Błąd: Słowo '{slowo}' już istnieje w bazie fiszek!")
            continue

        znaczenie = input(f"Podaj znaczenie dla '{slowo}': ").strip()
        fiszki[slowo] = znaczenie
        print(f"Dodano: {slowo} -> {znaczenie}\n")

    if not fiszki:
        print("Nie dodano żadnych słówek. Koniec programu.")
        return

    print("\n=== ETAP 2: QUIZ ===")
    print("Wpisz 'koniec', aby zakończyć test.\n")

    poprawne = 0
    bledne = 0
    lista_slow = list(fiszki.keys())

    while True:
        wylosowane_slowo = random.choice(lista_slow)
        poprawne_znaczenie = fiszki[wylosowane_slowo]

        odpowiedz = input(f"Jakie jest znaczenie słowa '{wylosowane_slowo}'? ").strip()

        if odpowiedz.lower() == "koniec":
            break

        if odpowiedz.lower() == poprawne_znaczenie.lower():
            print("Dobrze!\n")
            poprawne += 1
        else:
            print(f"Błąd! Prawidłowa odpowiedź to: '{poprawne_znaczenie}'\n")
            bledne += 1

    suma = poprawne + bledne
    print("\n=== PODSUMOWANIE WYNIKÓW ===")
    print(f"Liczba pytań: {suma}")
    print(f"Poprawne odpowiedzi: {poprawne}")
    print(f"Błędne odpowiedzi:   {bledne}")
    if suma > 0:
        skutecznosc = (poprawne / suma) * 100
        print(f"Skuteczność: {skutecznosc:.1f}%")

if __name__ == "__main__":
    program_fiszki()