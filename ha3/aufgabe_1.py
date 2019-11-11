def cube_root(value: float, e: float = 0.01):
    if e <= 0:
        return 0  # FIXME

    if 0 <= value < 1 or value <= -1:
        limit = (value, 1 if value > 0 else -1)
    else:
        limit = (1 if value > 0 else -1, value)
    
    guess = (limit[0] + limit[1]) / 2.0
    
    while abs(guess ** 3 - value) >= e:
        if guess ** 3 < value:
            limit = (guess, limit[1])
        else:
            limit = (limit[0], guess)
        
        guess = (limit[0] + limit[1]) / 2.0
    
    return guess


print(cube_root(-1000, 0.00000001))
