st = input('Bitte geben sie eine Zeichenkette zum Verschlüsseln ein >>>')
enc = int(input('Bitte geben sie den Encoding Integer ein >>>'))
out = ''
for i in st:
    out += chr(ord(i) + enc)

print(out)
