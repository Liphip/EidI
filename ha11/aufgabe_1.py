# Aufgabe 1
#
import random


def einfuegen(L, e):
    if len(L) == 0:
        return 0

    for i in range(1, len(L)):
        if L[i] >= e > L[i - 1]:
            return i


def sortiere(L):
    M = []
    N = L.copy()
    for e in N:
        M.insert(einfuegen(M, e), e)
    return M


if __name__ == '__main__':
    M = []
    for i in range(10):
        L = [random.randint(0, 10) for i in range(10)]
        N = sortiere(L)
        print(N, "|", L)
        M.append(N)
    for e in M:
        if e != sorted(e):
            print("Sort Failed @", e, " != ", sorted(e))
            break
    pass
