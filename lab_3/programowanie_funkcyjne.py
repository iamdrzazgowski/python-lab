from functools import reduce


def kwadrat(x):
    return x ** 2


print(kwadrat(5))


def concat(s1, s2="nie ma", s3="nic"):
    """ documentation """
    return s1 + " " + s2 + " " + s3


print(concat("Ala", s3="kota"))


def rozszerz(l=[], element=['x']):
    l.append(element)
    return l


print(rozszerz())


def rozszerz2(l=None, element=['x']):
    if l == None:
        l = []
    l.append(element)
    return l


print(rozszerz2())


def f(a, b=None):
    if b == None:
        b = a
    print(a, b)


f("Adrian")


def dlugosc(x):
    if type(x) in {str, list, tuple}:
        return len(x)
    elif type(x) in (int, float, complex):
        return abs(x)
    else:
        return None


print(dlugosc(-43.53))


def funkcja(*args, **kwargs):
    print(args)
    print(kwargs)


funkcja(4, "Ala", [1, 2, 3], s="error")


def f2(x):
    # global i  # zmiana wartości zmiennej globalnej
    return x ** i


i = 5
print(f2(3), i)

# funkcja lambda
# [argument]:[co z nim robimy]

szescian = lambda x: x ** 3
print(szescian(5))

func = lambda a, b, c=2: (a + b) ** c
print(func(1, 2, 4))


def szescian2(x):
    return x ** 3


lista = [i for i in range(1, 11)]
print(list(map(szescian2, lista)))

print(list(map(lambda x: x ** 3, lista)))


def select(x):
    if x > 0:
        return True
    return False


lista2 = [i * (-1) ** i for i in range(1, 21)]
print(list(filter(select, lista2)))
print(list(filter(lambda x: x > 0, lista2)))

lista3 = ["a", "b", "c", "d"]


def freduce(x, y):
    print(x, y)
    return x + y


print(reduce(freduce, lista3))

n = 30
print(reduce(lambda x, y: x + y, range(1, n + 1)))

lista4 = [7, 6, 3, 8, 3, 7, 9, 2, 6, 1, 0, 3, 2, 7]
print(sorted(lista4))
print(sorted(lista4, key=lambda i: i % 2))

lista5 = "Ala ma kota psa i chomika".split()
print(sorted(lista5, key=lambda x: len(x), reverse=False))

listaL = [1, 2, 3, 4]
listaR = [1, 2, 3, 4]


def ilsc(lista1, lista2):
    return sum(map(lambda x, y: x * y, lista1, lista2))

print(ilsc(listaL, listaR))

listaP = list(range(1,31))
print([i * 2 if i % 2 != 0 else i for i in list(filter(lambda x: x % 3 != 0, listaP))])
print(list(map(lambda i: 2*i if i % 2 else i, list(filter(lambda x: x % 3 != 0, listaP)))))

listaN = ["ala", "123", "pies98"]
print(list(''.join([i for i in j if i.isalpha()]) for j in listaN))
print(list(map(lambda j: ''.join(filter(lambda i: i.isalpha(),j)), listaN)))
