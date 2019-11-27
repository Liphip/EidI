def summiere(b: tuple) -> int:
    def ebenen_summiere(b: tuple, e: int) -> int:
        sum = 0
        sum += ebenen_summiere(b[0], e + 1) if type(b[0]) == tuple else b[0] * e
        sum += b[1] * e
        sum += ebenen_summiere(b[2], e + 1) if type(b[2]) == tuple else b[2] * e
        return sum
    return ebenen_summiere(b, 1)


def parse(s):
    return

print(summiere(((111,-16,-26),81,-7)))