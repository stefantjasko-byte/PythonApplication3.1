#1
kogus = 0

for i in range(15):
    arv = float(input("Sisesta arv: "))
    if arv == int(arv):
        kogus += 1

print("Täisarve on:", kogus)

#2
A = int(input("Sisesta A: "))
summa = 0

for i in range(1, A + 1):
    summa += i

print("Summa on:", summa)

korrutis = 1

#3
for i in range(8):
    arv = float(input("Sisesta arv: "))
    if arv > 0:
        korrutis *= arv

print("Korrutis on:", korrutis)

#4
for i in range(10, 21):
    print(i, "ruudus on", i ** 2)

    #5
    N = int(input("Mitu arvu sisestad? "))
summa = 0

#6
for i in range(N):
    arv = float(input("Sisesta arv: "))
    if arv < 0:
        summa += arv

print("Negatiivsete arvude summa:", summa)

N = int(input("Sisesta N: "))
neg = 0
pos = 0
null = 0

#7
for i in range(N):
    arv = float(input("Sisesta arv: "))

    if arv < 0:
        neg += 1
    elif arv > 0:
        pos += 1
    else:
        null += 1

print("Negatiivseid:", neg)
print("Positiivseid:", pos)
print("Nulle:", null)

A = int(input("Sisesta A: "))
B = int(input("Sisesta B: "))
K = int(input("Sisesta K: "))

for i in range(A, B + 1):
    if K != 0 and i % K == 0:
        print(i)

#8
for toll in range(1, 21):
    cm = toll * 2.5
    print(toll, "tolli =", cm, "cm")

S = float(input("Sisesta summa: "))
N = int(input("Sisesta aastate arv: "))

for i in range(N):
    S *= 1.03

print("Lõppsumma:", round(S, 2), "eurot")

#9
for i in range(10):
    A = float(input("Esimene arv: "))
    B = float(input("Teine arv: "))

    if A > B:
        print("Suurem:", A)
    elif B > A:
        print("Suurem:", B)
    else:
        print("Arvud on võrdsed")

#10
import random

K = random.randint(1, 9)
korrutis = 1

print("Juhuslik arv:", K)

for i in range(11, 100, 2):
    if i % K == 0:
        korrutis *= i
        print(i)

print("Korrutis:", korrutis)

#11
import random

K = random.randint(1, 10)
korrutis = 1

print("Juhuslik arv:", K)

for i in range(11, 100, 2):
    if i % K == 0:
        korrutis *= i
        print(i)

print("Korrutis:", korrutis)

#12
N = int(input("Niidukite arv: "))
m = float(input("Esimese niiduki tunnid: "))

summa = 0

for i in range(N):
    summa += m + i / 6

print("Kõikide niidukite töötunnid:", summa)

#13
summa = 0
kogus = 0

for i in range(100, 1001):
    if i % 7 == 0:
        print(i)
        summa += i
        kogus += 1

print("Arvude kogus:", kogus)
print("Summa:", summa)

#14
import random

N = random.randint(1, 10)
korrutis = 1

for i in range(1, N + 1):
    korrutis *= i

print("N =", N)
print("Korrutis:", korrutis)

#15
for i in range(10):
    for j in range(10):
        print(j, end=" ")
    print()

#16
for i in range(9):
    for j in range(9):
        if i == j:
            print(i + 1, end=" ")
        else:
            print(0, end=" ")
    print()

#17
N = int(input("Sisesta arv: "))

for i in range(1, 10):
    print(N, "*", i, "=", N * i)

#18
for i in range(20, 51):
    if i % 3 == 0 and i % 5 != 0:
        print(i)

#19
for i in range(35, 88):
    if i % 7 in [1, 2, 5]:
        print(i)

#20
summa = 0

for i in range(1, 51):
    if i % 5 == 0 or i % 7 == 0:
        summa += i

print("Summa:", summa)

#21
for i in range(10):
    x = float(input("Sisesta arv: "))
    if x < 0:
        x = abs(x)
    print(x)

#22
i = 100
s = 0

while True:
    if i % 17 == 0:
        s += i

    i += 1

    if i > 200:
        break

print("Summa:", s)

#23
N = int(input("Punktide arv: "))
a = float(input("Ringi keskpunkt a: "))
b = float(input("Ringi keskpunkt b: "))
R = float(input("Raadius R: "))

count = 0

for i in range(N):
    x = float(input("x: "))
    y = float(input("y: "))

    if (x - a)**2 + (y - b)**2 <= R**2:
        count += 1

print("Ringis olevaid punkte:", count)

#24
N = int(input("Õpilaste arv: "))
i = 0
s = 0

while i < N:
    pikkus = float(input("Sisesta pikkus cm: "))
    s += pikkus
    i += 1

if N > 0:
    print("Keskmine pikkus:", s / N)

#25
N = int(input("Sisesta N: "))
count = 0

for i in range(1, N + 1):
    if i % 2 != 0 and i % 3 != 0 and i % 5 != 0:
        count += 1

print("Arvude hulk:", count)

#26
for a in range(10, 100):
    for b in range(10, 100):
        arv = a * 100 + b

        if arv % (a * b) == 0:
            print(a, b, "->", arv)

#27
for A in range(10, 100):
    for B in range(10, 100):
        esimene = A * 100 + B
        teine = B * 100 + A

        if esimene % 99 == 0 and teine % 49 == 0:
            print("A =", A, "B =", B)

#28
import random

arv = random.randint(1, 100)
katsed = 0

while True:
    pakkumine = int(input("Arva arv 1-100: "))
    katsed += 1

    if pakkumine == arv:
        print("Õige! Arvasid ära!")
        break
    elif pakkumine < arv:
        print("Minu arv on suurem!")
    else:
        print("Minu arv on väiksem!")

print("Katseid:", katsed)

#29
for i in range(9):
    for j in range(9):
        if j == 0 or i == j:
            print("x", end=" ")
        else:
            print(0, end=" ")
    print()

#30
import random

M = random.randint(1, 20)
N = random.randint(1, 20)

print("M =", M, "N =", N)

for i in range(N, M + 1):
    print(i, end=" ")

print()

for i in range(M, N + 1):
    print(i, end=" ")

print()

#31
K = int(input("Kotletti arv: "))
M = int(input("Mitu kotletti mahub pannile: "))

if M > 0:
    tais = K // M
    jaak = K % M

    print("Täis pannitäisi:", tais)
    print("Viimasele pannile:", jaak)