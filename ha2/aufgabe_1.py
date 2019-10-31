"""
Copyright (c) 2019  Luis Michaelis, Philip Laskowicz
Licensed under MIT (https://opensource.org/licenses/mit-license.php).
"""

satz = input('In > ').lower()
vokal = input('Vokal > ').lower()

for i in ['a', 'e', 'i', 'o', 'u']:
    satz = satz.replace(i, vokal)

print(satz)
