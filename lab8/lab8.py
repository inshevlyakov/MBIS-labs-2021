import math

u = '12345'
v = '56789'
b = 10
n = 5

# A1

j = n
k = 0

w = list()
for i in range(1, n + 1):
    w.append((int(u[n - i]) + int(v[n - i]) + k) % b)
    k = (int(u[n - i]) + int(v[n - i]) + k) // b
    j = j - 1
w.reverse()
print(w)

# A2
u = '56789'
v = '12345'

j = n
k = 0
w = list()
for i in range(1, n + 1):
    w.append((int(u[n - i]) - int(v[n - i]) + k) % b)
    k = (int(u[n - i]) - int(v[n - i]) + k) // b
    j = j - 1
w.reverse()
print(w)

# A3
u = '123456'
v = '7890'
n = 6
m = 4

w = list()
for i in range(m + n):
    w.append(0)
j = m


def s6():
    global j
    global w
    j = j - 1
    if j > 0:
        s2()
    if j == 0:
        print(w)


def s2():
    global v
    global w
    global j
    if j == m:
        j = j - 1
    if int(v[j]) == 0:
        w[j] = 0
        s6()


def s4():
    global k
    global t
    global i
    if i == n:
        i = i - 1
    t = int(u[i]) * int(v[j]) + w[i + j] + k
    w[i + j] = t % b
    k = t / b


def s5():
    global i
    global w
    global j
    global k
    i = i - 1
    if i > 0:
        s4()
    else:
        w[j] = k


s2()
i = n
k = 0
t = 1
s4()
s5()
s6()
print(w)

# A4
u4 = '12345'
n = 5
v4 = '6789'
m = 4
b = 10
wl = list()
for i in range(m + n + 2):
    wl.append(0)
tl = 0
for sl in range(0, m + n):
    for il in range(0, sl + 1):
        if n - il > n or m - sl + il > m or n - il < 0 or m - sl + il < 0 or m - sl + il - 1 < 0:
            continue
        tl = tl + (int(u[n - il - 1]) * int(v[m - sl + il - 1]))
    wl[m + n - sl - 1] = tl & b
    tl = math.floor(tl / b)
    print(wl)

# A5
u = "12346789"
n = 7
v = "56789"
t = 4
b = 10
q = list()
for j in range(n - t):
    q.append(0)
r = list()
for j in range(t):
    r.append(0)

while int(u) >= int(v) * (b ** (n - t)):
    q[n - t] = q[n - t] + 1
    u = int(u) - int(v) * (b ** (n - t))
u = str(u)
for i in range(n, t + 1, -1):
    v = str(v)
    u = str(u)
    if int(u[i]) > int(v[t]):
        q[i - t - 1] = b - 1
    else:
        q[i - t - 1] = math.floor((int(u[i]) * b + int(u[i - 1])) / int(v[t]))

    while (int(q[i - t - 1]) * (int(v[t]) * b + int(v[t - 1])) > int(u[i]) * (b ** 2) + int(u[i - 1]) * b + int(
            u[i - 2])):
        q[i - t - 1] = q[i - t - 1] - 1
    u = (int(u) - q[i - t - 1] * b ** (i - t - 1) * int(v))
    if u < 0:
        u = int(u) + int(v) * (b ** (i - t - 1))
        q[i - t - 1] = q[i - t - 1] - 1
r = u
print(q, r)
