"""
Copyright (c) 2019  Luis Michaelis, Philip Laskowicz
Licensed under MIT (https://opensource.org/licenses/mit-license.php).
"""

decimal = input('Decimal > ')

# The following code could be made (REALLY) easily using:
#     bin(decimal)[2:]

if not decimal.isnumeric():
    print('Invalide Dezimalzahl!')
else:
    decimal = int(decimal)
    binary = ''
    
    # easier with math.log2(...)
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