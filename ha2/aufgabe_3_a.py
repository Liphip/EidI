"""
Copyright (c) 2019  Luis Michaelis, Philip Laskowicz
Licensed under MIT (https://opensource.org/licenses/mit-license.php).
"""

bin = input('Geben sie eine positive Binärzahl ein >>>')[::-1]

if bin.count('1') + bin.count('0') != len(bin) or len(bin) < 1 :
    print('Bitte gültige Binärzahl eingeben.')
    exit(-1)

dec = 0

for i in range(len(bin)):
    dec += int(bin[i]) * (2 ** i)

print(dec)
