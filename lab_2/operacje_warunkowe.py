# x = int(input("Podaj x: "))
# y = 5*(x == 10)

# if x > 5:
#     print(f'Wynik: {x}')
# else:
#     print("End")

# print(f'{y}')

# if x == 1:
#     print("Jeden")
# elif x == 2:
#     print("Dwa")
# else:
#     print("Więcej")
#
# if not x > 5 and y < 3:
#     print("OK")
#
# l = {1, 2, 3}

# if x in l:
#     print("Yes")
# else:
#     print("No")


# v = {True, True, False}
# any(v)
#
# z = int(input())
# x = z if z > 5 else 10*z
# print(f'Z: {x}')

s = "Ala ma kota"

# for i in s:
#     print(i, end="")

# for x in [1, 2, 3, 4, 5]:
#     print(f'{x**2}')

# for i in range(10, 0, -1):
#     print(i)

for i in range(20):
    if i % 2 == 0:
        continue

    print(i, end=" ")

dict = {"a": 10, "b": 20, "c": 25}
print(dict.get("b"))
