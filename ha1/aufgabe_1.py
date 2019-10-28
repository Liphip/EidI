try:
    width = int(input("Geben sie die Breite des Rechtecks an! "))
    hight = int(input("Geben sie die Höhe des Rechtecks an! "))
except:
    print("Bitte neustarten und Zahlenwert > 0 eingeben!")
    exit(-1)

if width <= 0 or hight <= 0:
    print("Bitte neustarten und Zahlenwert > 0 eingeben!")
    exit(-1)

x = (" " + ("-" * width) + " ")
y = ("|" + (" " * width) + "|\n")

print(x)
print(y * hight, end="")
print(x)
