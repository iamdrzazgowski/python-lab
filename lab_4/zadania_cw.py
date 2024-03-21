"""Zadanie 8"""
print(f'Zadanie 8')

lista = list(range(1,31))

# Użycie map i filter
print(list(map(lambda x: x * 2 if x % 2 == 0 else x,list(filter(lambda x: x % 3 != 0, lista)))))

# Lista składana
print(list([i * 2 if i % 2 == 0 else i for i in list([j for j in lista if j % 3 != 0])]))

"""Zadanie 9"""
print(f'Zadanie 9')

slowa = ["ala", "ma69", "3254"]

# Użycie map i filter
print(list(map(lambda x: ''.join(filter(str.isalpha, x)), slowa)))

# Lista składana
print(list(''.join([i for i in j if i.isalpha()]) for j in slowa))

"""  Zadanie 10  """
print(f'Zadanie 10')
# Użycie map i filter
print(list(map(int, filter(bool, map(lambda j: ''.join(filter(lambda i: i.isdigit(), j)), slowa)))))

# Lista składana
print([int(j) for j in [''.join([i for i in j if i.isdigit()]) for j in slowa] if j])

"""Zadanie 11"""

print(f'Zadanie 11')
lista_krotek = [(1,), (2, 3), (4, 5, 6), (7, 8, 6, 7), (3, 9, 12, 6)]

# Użycie map i filter
print(list(map(lambda krotka: tuple(krotka[:2]), filter(lambda krotka: len(krotka) >= 2, lista_krotek))))

# Lista składana
print(list([tuple(krotka[:2]) for krotka in lista_krotek if len(krotka) >= 2]))

"""Zadanie 12"""
print(f'Zadanie 12')

print(list(filter(lambda x: sum(x) % 2 == 0, lista_krotek)))

"""Zadanie 13"""
print(f'Zadanie 13')

print(list([krotka for krotka in lista_krotek if all(element % 3 == 0 for element in krotka)]))

"""Zadanie 14"""
print(f'Zadanie 14')

print(list([krotka for krotka in lista_krotek if any(element % 3 == 0 for element in krotka)]))

"""Zadanie 15"""
print(f'Zadanie 15')

lista_slow = ["Ala ma kota", "pies", "Jakub", "Opole Lubelskkie"]
print(list([element.split()[0] for element in lista_slow if ' ' in element]))

"""Zadanie 21"""

print(f'Zadanie 21')
def pole(*args):
    if len(args) == 1:
        return args[0] * args[0]
    elif len(args) == 2:
        return args[0] * args[1]
    elif len(args) == 3:
        return ((args[0] + args[1]) * args[2]) / 2
    else:
        return "Problem z argumentami"

print(pole(5, 7, 3))