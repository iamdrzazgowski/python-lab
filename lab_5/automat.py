import random

rule = 90
k = 38
n = 79

predict = ["***", "**_", "*_*", "*__", "_**", "_*_", "__*", "___"]
prerule = ["_" * int(i == '0') + "*" * int(i == '1') for i in f"{rule:08b}"]
automat = {key: value for (key, value) in zip(predict, prerule)}

cells = "_" * 31 + "*" + "_" * 31
n = len(cells)

for i in range(0, k):
    print(cells)
    cells = "".join(automat[cells[i - 1] + cells[i] + cells[(i + 1) * int(i < n - 1)]] for i in range(0, n))
