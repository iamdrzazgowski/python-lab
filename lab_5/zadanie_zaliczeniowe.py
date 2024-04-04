import random
def generate_initial_state(length):
    return ''.join(random.choice('*_') for _ in range(length))

# Zrobić słownik

automat = {
    "***": "*",
    "**_": "_"
}

s = "***__**_**_**_**_**"
s[1:4]

rule = input("Podaj ciąg binarny: ")
n = 8
k = 5
