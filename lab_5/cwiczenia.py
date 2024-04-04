# Formatowanie łańcuchów z wykorzystaniem mechanizmów formatowania

dane = (2, 'samochody', 2376.85, 2376.85)
print(dane[0], dane[1], "o masie", dane[2], "kilograma..")

s = "%d %s o masie %f kilograma \n(w notacji wykładniczej %e kilograma)"
print(s % dane)

print("*%10s*" % ("Hello"))
print("*%-10s*" % ("Hello"))

#Formatowanie liczb

print("*%10.4f*" % (2.6547657657))
print("*%-10.4f*" % (2.6547657657))

print("To jest %d%%." % (10))