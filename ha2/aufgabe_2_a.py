"""
Copyright (c) 2019  Luis Michaelis, Philip Laskowicz
Licensed under MIT (https://opensource.org/licenses/mit-license.php).
"""

st = input('Bitte geben sie eine Zeichenkette zum Verschlüsseln ein >>>')
enc = int(input('Bitte geben sie den Encoding Integer ein >>>'))
out = ''

for i in st:
    out += chr((ord(i) + enc) % 128)

print(out)
