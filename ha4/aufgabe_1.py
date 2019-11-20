"""
Copyright (c) 2019  Luis Michaelis, Philip Laskowicz
Licensed under MIT (https://opensource.org/licenses/mit-license.php).
"""


def anzahl(n: int) -> int:
    """ Was zu beweisen ist. """
    
    if n == 0:
        return 1
    
    return sum([anzahl(i) * anzahl(n - i - 1) for i in range(0, n)])
