def maximiere(s: str, k: int) -> str:
    def vertausche(s: str, i: int, j: int) -> str:
        return s[0:i] + s[j] + s[i + 1:j] + s[i] + s[j + 1:len(s)]

    def sortiere(s: str) -> str:
        return "".join((sorted(s)[::-1]))

    if k == 1:
        return vertausche(s, k - 1, s.rindex(sortiere(s)[k - 1]))
    else:
        x = maximiere(s, k - 1)
        return vertausche(x, k - 1, x.rindex(sortiere(x)[k - 1]))
