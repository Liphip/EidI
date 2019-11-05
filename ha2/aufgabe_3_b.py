try:
    dec = int(input('Bitte geben sie einen Dezimalzahl ein >>>'))
except:
    print('Bitte gültige Dezimalzahl eingeben.')
    exit(-1)

bin = ''

if dec % 2 == 0:
    dec = dec // 2

while dec > 0:
    bin += str(dec % 2)
    dec = dec // 2

print(bin)
