import random

matrix = [[0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0]]

for i in range(5):
    for j in range(5):
        matrix[i][j] = random.randint(-5,5)

print("Macierz 5x5")

maxTab = []
minTab = []

for j in range(5):
    max = 0
    min = 0
    for i in range(5):
        if matrix[i][j] > max:
            max = matrix[i][j]
        if matrix[i][j] < min:
            min = matrix[i][j]

    maxTab.append(max)
    minTab.append(min)


for i in range(5):
    for j in range(5):
        print(f"{matrix[i][j]:2}", end=" ")

    print("|")

print("=" * 15 + "|")

for i in range(5):
    print(f"{maxTab[i]:2}", end=" ")

print("| Maksymalna wartość kolumny")

for i in range(5):
    print(f"{minTab[i]:2}", end=" ")

print("| Minimalna wartość kolumny")