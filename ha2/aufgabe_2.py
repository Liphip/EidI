st = input('Bitte geben sie eine Zeichenkette zum Verschlüsseln ein >>>')
enc = int(input('Bitte geben sie den Encoding Integer ein >>>'))

for i in range(len(st)):
    print(i, st[i])
    st[i] = chr(ord(st[i]) + enc)

print(st)
