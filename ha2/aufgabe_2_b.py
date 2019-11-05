st = input('Bitte geben sie eine Zeichenkette zum Entschlüsseln ein >>>')
enc = int(input('Bitte geben sie den Encoding Integer ein >>>'))
out = ''
for i in st:
    out += chr((ord(i) - enc) % 127)

print(out)