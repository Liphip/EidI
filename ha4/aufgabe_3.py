def smaller1(i: float) -> float:
    return i - 34 if i - 34 > 0 else i


def smaller2(i: float) -> float:
    return (i - 11) / 2 if (i - 11) / 2 > 0 else i


def mini(i: float) -> float:
    return min(smaller1(i), smaller2(i))


def smaller(i: float) -> float:
    if mini(i) < i:
        return smaller(mini(i))

    else:
        return i


bt = float(input('Bitte größten Baum angeben >>>'))

print(smaller(bt))
