"""
Copyright (c) 2019  Luis Michaelis, Philip Laskowicz
Licensed under MIT (https://opensource.org/licenses/mit-license.php).
"""

a = abs(int(input('Geben sie die Breite des Rechtecks an > ')))
b = abs(int(input('Geben sie die Höhe des Rechtecks an > ')))

print(' ' + ('-' * a) + ' ')
print(('|' + (' ' * a) + '|\n') * b, end='')
print(' ' + ('-' * a) + ' ')
