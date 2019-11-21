"""
Copyright (c) 2019  Luis Michaelis, Philip Laskowicz
Licensed under MIT (https://opensource.org/licenses/mit-license.php).
"""


def height(x: float) -> float:
    a = x if x - 34 <= 0 else height(x - 34)
    b = x if (x - 11) / 2 <= 0 else height((x - 11) / 2)
    
    return a if a < b else b


print(height(float(input('Höhe > '))))
