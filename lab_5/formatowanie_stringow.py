# Formatowanie łańcuchów z wykorzystaniem mechanizmów formatowania

dane = (2, 'samochody', 2376.85, 2376.85)
print(dane[0], dane[1], "o masie", dane[2], "kilograma..")

s = "%d %s o masie %f kilograma \n(w notacji wykładniczej %e kilograma)"
print(s % dane)

print("*%10s*" % ("Hello"))
print("*%-10s*" % ("Hello"))

# Formatowanie liczb

print("*%10.4f*" % (2.6547657657))
print("*%-10.4f*" % (2.6547657657))

print("To jest %d%%." % (10))

# Metoda format

s = "{1} i {0} {zwierzeta}"
print(s.format(2, "psy", zwierzeta="koty"))

s = "elementy listy {lista[1]} i wartości ze słownika: {slownik[b]}"
print(s.format(lista=[1, 2, 3], slownik={"a": "Ala", "b": "Bolek"}))

# Formatowanie do prawej
print("|{1:>11s}|".format("Hello", "world"))

# Formatowanie do lewej
print("|{1:<11s}|".format("Hello", "world"))

# Formatowanie do środka
print("|{1:^11s}|".format("Hello", "world"))

print("{0:_^20.5f}".format(3.141592653589793))

# F łańcuch

x1 = 2
s1 = f"Długość wynosi {x1}."
s2 = f"Pole wynosi {(x2 := x1 ** 2)}."
x1 = 3
s3 = f"Jeszcze raz, pole wynosi {x2}"
print(s1)
print(s2)
print(s3)

e = 2.718378454
print(f"{e:*^14.2f}")
