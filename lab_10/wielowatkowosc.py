from time import sleep
from threading import Thread


def old_print(*x):
    for i in x:
        print(i, end="")
        sleep(1e-5)
    print()
    sleep(1e-5)


def f(n):
    for i in range(n):
        old_print(i)


thread1 = Thread(target=f, args=(5,))
thread2 = Thread(target=f, args=(5,))

thread1.start()
thread2.start()

old_print("End")
