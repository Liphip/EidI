leerbaum = ()


def init2():
    begriffe = ["a", "an", "and", "by", "effects", "for", "from", "high", "in", "of", "on", "the", "to", "with"]
    haeufigkeit = [32, 7, 69, 13, 6, 15, 10, 8, 64, 142, 22, 79, 18, 9]
    return (len(begriffe), begriffe, haeufigkeit)


def gg(baum: list, faktor: int = 1):
    if baum == leerbaum:
        return 0
    else:
        return faktor * haeufigkeit[baum[1]] + gg(baum[0], faktor + 1) + gg(baum[2], faktor + 1)


def loeseRekursiv(i: int = 0, j: int = len(begriffe), wb: dict = {}):
    if (i, j) in wb:
        return wb[(i, j)]
    if i == j:
        wb[(i, j)] = leerbaum
        return leerbaum
    if j == i + 1:
        wb[(i, j)] = (leerbaum, i, leerbaum)
        return (leerbaum, i, leerbaum)
    else:
        baum = (leerbaum, i, loeseRekursiv(i + 1, j))
        for k in range(i + 1, j):
            links = loeseRekursiv(i, k)
            rechts = loeseRekursiv(k + 1, j)
            if gg((links, k, rechts)) < gg(baum):
                baum = (links, k, rechts)
        wb[(i, j)] = baum
        return baum


(n, begriffe, haeufigkeit) = init2()

print(loeseRekursiv(0, len(begriffe), {}))
