"""
Copyright (c) 2019  Luis Michaelis, Philip Laskowicz
Licensed under MIT (https://opensource.org/licenses/mit-license.php).
"""

binary_reversed = input('Binary > ')[::-1]

if not binary_reversed.isnumeric() or len(binary_reversed) == 0:
    print('Invalide Binärzahl!')
else:
    decimal = 0
    for i in range(len(binary_reversed)):
        decimal += int(binary_reversed[i]) * (2 ** i)
    
    print(decimal)
