# start_point = "██ █    █  █   █     █      ██"

#Choinka

n = int(input("Podaj n: "))

# for i in range(1, n+1):
#     print(" " * (n - i) + "#" * (2 * i - 1))
#     if i == n:
#         print(" " * (n-3), "||")

for i in range(n + 1):
    print(" " * (n-i) + "*" * (i == 0) + "#" * (2*i+1) * (i > 0))
print(" " * (i-1) + "| |")