import random

def generate_initial_state(length):
    return ''.join(random.choice('*_') for _ in range(length))

def change_rules(automat_rules, rules):
    index = 0
    for key in automat_rules.keys():
        value = "-"

        if rules[index] == "0":
            value = "_"
        elif rules[index] == "1":
            value = "*"

        automat_rules[key] = value
        index += 1

    return automat_rules


def automat(rule, k, automat_rules):

    word = rule
    for j in range(k):
        new_code = ""
        for i in range(0, len(word)):

            if i == 0:
                new_code += automat_rules[word[-1] + word[i] + word[i+1]]
            elif i == len(word)-1:
                new_code += automat_rules[word[i-1] + word[i] + word[0]]
            else:
                new_code += automat_rules[word[i-1] + word[i] + word[i + 1]]

        print(f"{j + 1}) Result: {new_code}")
        word = new_code


rule = input("Enter the rule: ")
n = int(input("Enther the length of the sequence: "))
k = int(input("Enter the number of steps: "))

automat_rules = {
    "***": "_",
    "**_": "*",
    "*_*": "_",
    "*__": "*",
    "_**": "*",
    "_*_": "_",
    "__*": "*",
    "___": "_"
}


changed_rules = change_rules(automat_rules, rule)
word = generate_initial_state(n)
print("Generated code: ", word)
automat(word, k, changed_rules)
