def summiere(b: tuple) -> int:

    def ebenen_summiere(b: tuple, e: int) -> int:

        sum = ebenen_summiere(b[0], e + 1) if type(b[0]) == tuple else b[0] * (e + 1)
        sum += b[1] * e
        sum += ebenen_summiere(b[2], e + 1) if type(b[2]) == tuple else b[2] * (e + 1)

        return sum

    return ebenen_summiere(b, 1)


def parse(s:str) -> tuple:
    typ = ('(' , ',' , '-', ')')

    if s[0] != typ[0] or s[-1] != typ[-1]:
        return None
    else:

        tree = ()
    return


if __name__ == '__main__':
    print(summiere(((111, -16, -26), 81, -7)))
