"""
Copyright (c) 2019  Luis Michaelis, Philip Laskowicz
Licensed under MIT (https://opensource.org/licenses/mit-license.php).
"""


def cube_root(value: float, e: float = 0.01) -> float:
    if e <= 0:
        exit('e darf nicht weniger als 0 sein.')

    if value == 0:
        return 0

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
