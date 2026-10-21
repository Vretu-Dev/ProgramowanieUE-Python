import random

lista = []
biggerThanSrednia = 0
lowerThanSrednia = 0

for i in range(11):
    losowa = random.randint(-10,10)
    lista.append(losowa)

print("Elementy listy", lista)
print("Maksymalna Wartość", max(lista))
print("Minimalna Wartość", min(lista))
srednia = sum(lista) / len(lista)
print("Średnia Arytm", srednia)


for i in lista:
    if i > srednia:
        biggerThanSrednia += 1
    else:
        lowerThanSrednia += 1

print("Elementy większe od średniej (ilość)", biggerThanSrednia)
print("Elementy mniejsze od średniej (ilość)", lowerThanSrednia)

odwrotna = lista[::-1]
print(odwrotna)