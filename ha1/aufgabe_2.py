try:
    x12 = int(input("Geben sie eine zweistellige Zahl an! "))
except:
    print("Bitte neustarten und zeistellien Zahlenwert eingeben!")
    exit(-1)

if 99 < x12 < 10:
    print("Bitte neustarten und zeistellien Zahlenwert eingeben!")
    exit(-1)

x1 = int(x12 // 10)
x2 = int(x12 % 10)

out = x1 + x2

print(str(out) * out)
