waga = float(input("Podaj waga: "))
wzrost = float(input("Podaj wzrost: "))

wzrost = wzrost / 100

bmi = waga / (wzrost * wzrost)

if bmi >= 18.5 and bmi <= 24.9:
    print(f"Waga prawidłowa | BMI = {bmi}")
elif bmi > 24.9:
    print(f"Nadwaga | BMI = {bmi}")
else:
    print(f"Niedowaga | BMI = {bmi}")