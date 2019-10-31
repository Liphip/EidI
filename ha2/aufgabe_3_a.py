"""
Copyright (c) 2019  Luis Michaelis, Philip Laskowicz
Licensed under MIT (https://opensource.org/licenses/mit-license.php).
"""

binary_reversed = input('Binary > ')[::-1]

# The following code could be made (REALLY) easily using:
#     int(binary, base=2)

if binary_reversed.count('0') + binary_reversed.count('1') != len(binary_reversed) or len(binary_reversed) == 0:
    print('Invalide Binärzahl!')
else:
    decimal = 0
    for i in range(len(binary_reversed)):
        decimal += int(binary_reversed[i]) * (2 ** i)
    
    print(decimal)