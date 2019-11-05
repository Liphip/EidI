"""
Copyright (c) 2019  Luis Michaelis, Philip Laskowicz
Licensed under MIT (https://opensource.org/licenses/mit-license.php).
"""

decimal = input('Decimal > ')

if not decimal.isnumeric() or len(decimal) == 0:
    print('Invalide Dezimalzahl!')
else:
    decimal = int(decimal)
    binary = ''
    
    k = 0
    while 2**k < decimal:
        k += 1
    
    while len(binary) < k:
        p = 2**(k - len(binary) - 1)
        
        if decimal - p >= 0:
            binary += '1'
            decimal -= p
        else:
            binary += '0'
    
    print(binary)
