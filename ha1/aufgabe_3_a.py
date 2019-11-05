x = int(input("Geben sie die Stunden ihrer aktuellen Uhrzeit an > "))
y = int(input("Geben sie die Minuten ihrer aktuellen Uhrzeit an > "))
z = int(input("Geben sie die Zeit, die sie im Flugzeug verbarcht haben in Minuten ein > "))
print("%02d:%02d" % (((((x * 60) + y) - z ) % (24 * 60)) // 60, ((((x * 60) + y) - z ) % (24 * 60)) % 60), "\n" + "%02d:%02d" % (((((((x * 60) + y) - z ) % (24 * 60)) - 30) % (24 * 60)) // 60, ((((((x * 60) + y) - z ) % (24 * 60)) - 30) % (24 * 60)) % 60))