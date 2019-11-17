def intSuperlist(inp: list) -> bool:
    if len(inp) == 0:
        return False
    for i in inp:
        if type(i) == list and type(i) != intSuperlist(i):
            return False
        elif type(i) != int and type(i) != list:
            return False
    return True


def copy(inp: list) -> list:
    return [(i if type(i) == int else copy(i)) for i in inp]
