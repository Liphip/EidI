def count(i: int) -> int:
    if i == 0:
        return 1

    n = 0

    for j in range(0, i):
        n += count(j) * count(i - j - 1)

    return n
