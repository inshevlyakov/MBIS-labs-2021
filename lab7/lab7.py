def euclid(a, b):
    if b == 0:
        return a, 1, 0
    else:
        d, xx, yy = euclid(b, a % b)
        x = yy
        y = xx - (a // b) * yy
        return d, x, y


def inver(a, n):
    return euclid(a, n)[1]


def pol_ab(x, a, b, todochan):
    (G, H, P, Q) = todochan
    sub = x % 3
    if sub == 0:
        x = x * todochan[0] % todochan[2]
        a = (a + 1) % Q
    if sub == 1:
        x = x * todochan[1] % todochan[2]
        b = (b + 1) % todochan[2]
    if sub == 2:
        x = x * x % todochan[2]
        a = a * 2 % todochan[3]
        b = b * 2 % todochan[3]
    return x, a, b


def pollrad(G, H, P):
    Q = int((P - 1) // 2)
    x = G * H
    a = 1
    b = 1
    X = x
    A = a
    B = b
    for i in range(1, P):
        x, a, b = pol_ab(x, a, b, (G, H, P, Q))
        X, A, B = pol_ab(X, A, B, (G, H, P, Q))
        X, A, B = pol_ab(X, A, B, (G, H, P, Q))
        if x == X:
            break
    nom = a - A
    denom = B - b
    res = (inver(denom, Q) * nom) % Q
    if ver(G, H, P, res):
        return res


def ver(g, h, p, x):
    return pow(g, x, p) == h

def lab7():
    args = [
        (11, 44, 107),
    ]
    for arg in args:
        res = pollrad(*arg)
        print(arg, ': ', res)
        print('Valid: ', ver(arg[0], arg[1], arg[2], res), end='\n')

lab7()