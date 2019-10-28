x = int(input("Geben sie die Stunden ihrer aktuellen Uhrzeit an > "))
y = int(input("Geben sie die Minuten ihrer aktuellen Uhrzeit an > "))
z = int(input("Geben sie die Zeit, die sie im Flugzeug verbarcht haben in Minuten ein > "))

departure = ((x * 60) + y) - z
departure %= 24 * 60
print("%02d:%02d" % (departure // 60, departure % 60))

boarding = (departure - 30) % (24 * 60)
print("%02d:%02d" % (boarding // 60, boarding % 60))