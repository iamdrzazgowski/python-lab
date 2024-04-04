# Formatowanie łańcuchów z wykorzystaniem mechanizmów formatowania

dane = (2, 'samochody', 2376.85, 2376.85)
print(dane[0], dane[1], "o masie", dane[2], "kilograma..")

s = "%d %s o masie %f kilograma \n(w notacji wykładniczej %e kilograma)"
print(s % dane)