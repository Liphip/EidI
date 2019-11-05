try:
    dec = int(input('Bitte geben sie einen Dezimalzahl ein >>>'))
except:
    print('Bitte gültige Dezimalzahl eingeben.')
    exit(-1)

bin = ''
gerade = False

if dec % 2 == 0:
    gerade = True

while dec > 1:
    bin += str(dec % 2)
    dec = dec // 2
    print(bin)

bin = '1' + bin[::-1]

print(bin)
