a = abs(int(input('Geben sie die Breite des Rechtecks an > ')))
b = abs(int(input('Geben sie die Höhe des Rechtecks an > ')))

print(' ' + ('-' * a) + ' ')
print(('|' + (' ' * a) + '|\n') * b, end='')
print(' ' + ('-' * a) + ' ')
