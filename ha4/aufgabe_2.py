def intSuperlist(inp: list) -> bool:
    if len(inp) == 0:
        return False
    for i in inp:
        if type(i) != int and type(i) != list:
            return False
        elif type(i) == list and type(i) != int:
            return intSuperlist(i)
    return True


def copy(inp: list) -> list:
    ret = []
    print(type(inp))
    if type(inp) == list and len(inp) != 0:
        for i in range(len(inp)):
            print(type(inp[i]), ret)
            if type(inp[i]) != list:
                ret += inp[i]
            elif type(inp[i]) == list:
                ret += copy(inp[i])
    else:
        ret += inp
    return ret


ar = [[[1, [2, 3], 1, [[1]], 2], 6], 4]

print(intSuperlist(ar), copy(ar), copy(ar) == ar)
