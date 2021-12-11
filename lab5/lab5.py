import random


def ferma(n, count):
    for i in range(count):
        a = random.randint(2, n - 1)
        if a ** (n - 1) % n != 1:
            print('Not Simple')
            return False
    print('Simple')
    return True


def bin_exp(base, exponent, mod):
    x = 1
    y = base
    while exponent > 0:
        if exponent % 2 == 1:
            x = (x * y) % mod
        y = (y * y) % mod
        exponent = exponent // 2
    return x % mod


def jacob(a, n):
    if a == 0:
        return 0
    ans = 1
    if a < 0:
        a = -a
        if n % 4 == 3:
            ans = -ans
    if a == 1:
        return ans
    while a:
        if a < 0:
            a = -a
            if n % 4 == 3:
                ans = -ans
        while a % 2 == 0:
            a = a // 2
            if n % 8 == 3 or n % 8 == 5:
                ans = -ans
        a, n = n, a
        if a % 4 == 3 and n % 4 == 3:
            ans = -ans
        a = a % n
        if a > n // 2:
            a = a - n
    if n == 1:
        return ans
    return 0


def strassen(p, iter):
    if p < 2:
        return False
    if p != 2 and p % 2 == 0:
        return False
    for i in range(iter):
        a = random.randrange(p - 1) + 1
        jacobian = (p + jacob(a, p)) % p
        mod = bin_exp(a, (p - 1) / 2, p)
        if jacobian == 0 or mod != jacobian:
            return False

def miller_rabin(n):
    if n != int(n):
        print('Not Simple')
        return False
    n = int(n)
    if n == 0 or n == 1 or n == 4 or n == 6 or n == 8 or n == 9:
        print('Not Simple')
        return False
    if n == 2 or n == 3 or n == 5 or n == 7:
        print('Simple')
        return True
    s = 0
    d = n - 1
    while d % 2 == 0:
        d >>= 1
        s += 1
    assert (2 ** s * d == n - 1)

    def trial(a):
        if pow(a, d, n) == 1:
            print('Not Simple')
            return False
        for i in range(s):
            if pow(a, 2 ** i * d, n) == n - 1:
                print('Not Simple')
                return False
        print('Simple')
        return True

    for i in range(8):
        a = random.randrange(2, n)
        if trial(a):
            print('Not Simple')
            return False
        print('Simple')
        return True

def lab5():
    n = int(input('Input a number (Ferma):\n'))
    print('Test Ferma for ', n)
    ferma(n, 600)
    n = int(input('Input a number (Miller-Rabin):\n'))
    print('Test Miller-Rabin for ', n)
    miller_rabin(n)
    n = int(input('Input a number (Solovei-Strassen):\n'))
    if strassen(n, 600):
        print(n, ' - Simple')
    else:
        print(n, ' - Not Simple')

lab5()