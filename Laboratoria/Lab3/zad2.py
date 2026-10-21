import random

lista = []
for i in range(21):
    losowa = random.randint(1,10)
    lista.append(losowa)

print(lista)

freq = [0] * 11
for i in lista:
    freq[i] += 1

for i in range(1, 11):
    print(i, freq[i])