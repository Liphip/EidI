"""
Copyright (c) 2019  Luis Michaelis, Philip Laskowicz
Licensed under MIT (https://opensource.org/licenses/mit-license.php).
"""

bin = input('Geben sie eine positive Binärzahl ein >>>')

try:
    test = int(bin, 2)
    if test < 1:
        print('Bitte gültige Binärzahl eingeben.')
        exit(-1)

except ValueError:
    print('Bitte gültige Binärzahl eingeben.')
    exit(-1)

dec = 0

for i in range(len(bin)):
    dec += int(bin[i]) * (2 ** i)

print(dec)
