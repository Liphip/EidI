def maxmult_lin(L: list) -> int:
    a, b = 0, 0
    
    for elem in L:
        if elem > a and a < b:
            a = elem
        elif elem > b:
            b = elem
    
    return a * b


print(maxmult_lin([100, 101, 0, 2, 55, 22, 92]))