from math import gcd

ag = 1
bg = 1


def func(x, n):
    return (x * x + 5) % n


def func_2(n, a, b, d):
    a = func(a, n) % n
    b = func(func(b, n), n) % n
    d = gcd(a - b, n)
    if 1 < d < n:
        p = d
        print(p)
        exit()
    if d == n:
        print('Not found')
    if d == 1:
        global ag
        ag = b
        func_2(n, a, b, d)


def lab6():
    n = 1024
    c = 1
    a = c
    b = c
    a = func(a, n) % n
    b = func(a, n) % n
    d = gcd(a - b, n)
    if 1 < d < n:
        p = d
        print(p)
        exit()
    if d == n:
        pass
    if d == 1:
        func_2(n, a, b, d)


lab6()
