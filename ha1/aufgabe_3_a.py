try:
    x = int(input("Geben sie die Stunden ihrer aktuellen Uhrzeit an! "))
    y = int(input("Geben sie die Minuten ihrer aktuellen Uhrzeit an! "))
    z = int(input("Geben sie die Zeit, die sie im Flugzeug verbarcht haben in Minuten ein! "))
except:
    print("Bitte neustarten und zweistelligen Zahlenwert mit 0<=Stunden<=23 und 0<=Minuten<=59 und einen Zahlenwert mit"
          " 0<=Flugzeit eingeben!")
    exit(-1)

if 0 <= x <= 23 or 0 <= y <= 59 or 0 <= z:
    print("Bitte neustarten und zweistelligen Zahlenwert mit 0<=Stunden<=23 und 0<=Minuten<=59 und einen Zahlenwert mit"
          " 0<=Flugzeit eingeben!")
    exit(-1)

timeMin = ((x * 60) + y)
departure = (timeMin - z)

if (departure > 0):
    print(str(departure // 60) + ":" + str(departure % 60))
else:
    departure = ((24 * 60) + departure)
    print(str(departure // 60) + ":" + str(departure % 60))

boarding = (departure - 30)

if (boarding > 0):
    print("%02d:%02d" % (boarding // 60, boarding % 60))
else:
    boarding = ((24 * 60) + boarding)
    print("%02d:%02d" % (boarding // 60, boarding % 60))
