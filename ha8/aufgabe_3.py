def det(M):
    a = (M[0])[0]
    b = (M[1])[0]
    c = (M[2])[0]
    d = (M[0])[1]
    e = (M[1])[1]
    f = (M[2])[1]
    g = (M[0])[2]
    h = (M[1])[2]
    i = (M[2])[2]
    return a * e * i + b * f * g + c * d * h - g * e * c - h * f * a - i * d * b


def ausgabe(M):
    return


def aufzaehlen(b):
    return [[[a, j, c], [d, e, f], [g, h, i]] for a in range(b + 1) for j in range(b + 1) for c in range(j + 1) for d in
            range(j + 1) for e in range(j + 1) for f in range(j + 1) for g in range(j + 1) for h in range(j + 1) for i
            in range(j + 1) if det([[a, b, c], [d, e, f], [g, h, i]]) == 0]


if __name__ == "__main__":
    pass
