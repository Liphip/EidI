"""
Copyright (c) 2019  Luis Michaelis, Philip Laskowicz
Licensed under MIT (https://opensource.org/licenses/mit-license.php).
"""


def summiere(b: tuple) -> int:
    def ebenen_summiere(b: tuple, e: int) -> int:
        sum = ebenen_summiere(b[0], e + 1) if type(b[0]) == tuple else b[0] * (e + 1)
        sum += b[1] * e
        sum += ebenen_summiere(b[2], e + 1) if type(b[2]) == tuple else b[2] * (e + 1)

        return sum

    return ebenen_summiere(b, 1)

# def parse(s:str) -> tuple:
#    return
