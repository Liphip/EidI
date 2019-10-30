a = abs(int(input('Geben sie die Breite des Rechtecks an > ')))
b = abs(int(input('Geben sie die Höhe des Rechtecks an > ')))
print((' ' + ('-' * a) + ' ') + ('|' + (' ' * a) + '|\n') * b + (' ' + ('-' * a) + ' '), end='')

