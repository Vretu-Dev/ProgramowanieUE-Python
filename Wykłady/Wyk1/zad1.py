# 21.10.2026

# Wszystko jest obiektem
# Odwołanie do zmiennej typu złożonego, jest wskaźnikiem (referencja)
#

# Typy prosty

# int
a = 99
# float
b = 1.14
# bool
prawda = True

# Typy złożone
c = "Ala"
print(type(c))

# Listy
l = [1,2,3]
# Przykład
a = 4
b = a
a += 1


print(a,b)

l = [2,1]
l2 = l
l[0] += 1

print(l,l2)
print(id(a),id(b))
print(id(l),id(l2))


s = "Ala ma kota"
s2 = s
s += " i psa."

print(s,s2)

#
a = 5
b = 11
x = a&b
print(x)
y = a | b
print(y)

# Funkcje
def dodawanie(a:int,b:int) -> str:
    suma = a + b
    return f"Dodawanie wynosi {suma}"

print(dodawanie("d","d"))


ala = print
print = 123

ala(1)