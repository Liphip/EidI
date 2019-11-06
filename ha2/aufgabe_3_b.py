"""
Copyright (c) 2019  Luis Michaelis, Philip Laskowicz
Licensed under MIT (https://opensource.org/licenses/mit-license.php).
"""

dec = input('Bitte geben sie einen Dezimalzahl ein >>>')

if not dec.isnumeric():
    print('Bitte gültige Dezimalzahl eingeben.')
    exit(-1)

dec = int(dec)
bin = ''

while dec > 1:
    bin += str(dec % 2)
    dec = dec // 2

bin = (('1' + bin[::-1]) if dec != 0 else '0')

print(bin)
