def einlesen(n, pos):
    return [[0 if (i, j) == pos else -1 for j in range(n)] for i in range(n)]


def possible_moves(tupel, n):
    directions = [(tupel[0] + 1, tupel[1] + 2),
                  (tupel[0] - 1, tupel[1] + 2),
                  (tupel[0] + 1, tupel[1] - 2),
                  (tupel[0] - 1, tupel[1] - 2),
                  (tupel[0] + 2, tupel[1] + 1),
                  (tupel[0] - 2, tupel[1] + 1),
                  (tupel[0] + 2, tupel[1] - 1),
                  (tupel[0] - 2, tupel[1] - 1)]
    return [i for i in directions if n > i[0] >= 0 and n > i[1] >= 0]


def min_moves(brett, position, n):
    for i in possible_moves(position, len(brett)):
        lat = brett[i[0]]
        lon = lat[i[1]]
        if n < lon or lon < 0:
            lat[i[1]] = n
            min_moves(brett, i, n + 1)
    return brett


if __name__ == "__main__":
    pass
    size = 8
    position = (4, 4)
    print(min_moves(einlesen(size, position), position, 1))
