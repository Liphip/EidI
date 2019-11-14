def anzahl(n: int) -> int:
    """ Was zu beweisen ist. """
    
    if n == 0:
        return 1
    
    value = 0
    for i in range(0, n):
        value += anzahl(i) * anzahl(n - i - 1)
    
    return value


print(anzahl(2))
