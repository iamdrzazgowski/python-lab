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
    global i  # zmiana wartości zmiennej globalnej
    i = 3
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
    if x % 2 == 0:
        return True
    return False

print(list(filter(select, lista)))
