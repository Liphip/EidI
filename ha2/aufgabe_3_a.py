"""
Copyright (c) 2019  Luis Michaelis, Philip Laskowicz
Licensed under MIT (https://opensource.org/licenses/mit-license.php).
"""

binary = input('Geben sie eine positive Binärzahl ein >>> ')[::-1]

if binary.count('1') + binary.count('0') != len(binary) or len(binary) < 1:
    print('Bitte gültige Binärzahl eingeben.')
    exit(-1)

dec = 0

for i in range(len(binary)):
    dec += int(binary[i]) * (2 ** i)

print(dec)
