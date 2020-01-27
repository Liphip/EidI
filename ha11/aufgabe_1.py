"""
Copyright (c) 2019  Luis Michaelis, Philip Laskowicz
Licensed under MIT (https://opensource.org/licenses/mit-license.php).
"""


# Aufgabe 1
#

def einfuegen(L, e):
    a, b = 0, len(L)

    if len(L) == 0:
        return 0

    while True:
        p = (a + b) // 2

        if L[p - 1] < e < L[p + 1]:
            return L, p + 1 if L[p] < e else p

        elif L[p] < e:
            a = p
        elif L[p] > e:
            b = p


def sortiere(L):
    sort = []

    for i in L:
        sort.insert(einfuegen(sort, i)[1], i)

    return sort


if __name__ == '__main__':
    x = [1, 2, 3, 4, 7, 8, 9, 11]
    x.insert(einfuegen(x, 6)[1], 6)

    print(x)
