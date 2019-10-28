x = input("Geben sie eine zweistellige Zahl an > ")

if len(x) != 2:
    print("Bitte neustarten und zeistellien Zahlenwert eingeben!")
    exit(-1)

out = int(x[0]) + int(x[1])
print(str(out) * out)
