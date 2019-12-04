leerbaum = ()
begriffe = ["a", "an", "and", "by", "effects", "for", "from", "high", "in", "of", "on", "the", "to", "with"]
haeufigkeit = [32, 7, 69, 13, 6, 15, 10, 8, 64, 142, 22, 79, 18, 9]


def gg(baum, faktor = 1):
    if baum == leerbaum:
        return 0
    else:
        return faktor * haeufigkeit[baum[1]] + gg(baum[0], faktor + 1) + gg(baum[2], faktor + 1)


def loeseRekursiv(i, j, wb):
    if i == j:
        return leerbaum
    if j == i + 1:
        return (leerbaum, i, leerbaum)
    else:
        baum = (leerbaum, i, loeseRekursiv(i + 1, j))
        for k in range(i + 1, j):
            links = loeseRekursiv(i, k)
            rechts = loeseRekursiv(k + 1, j)
            if gg((links, k, rechts)) < gg(baum):
                baum = (links, k, rechts)
        return baum
