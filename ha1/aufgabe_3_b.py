try:
    x = int(input("Geben sie die Stunden ihrer geschätzten Ankuftszeit an! "))
    y = int(input("Geben sie die Minuten ihrer geschätzten Ankuftszeit an! "))
except:
    print("Bitte neustarten und zweistelligen Zahlenwert mit 0<=Stunden<=23 und 0<=Minuten<=59 eingeben!")
    exit(-1)

if 23 <= x <= 0 or 59 < y < 0:
    print("Bitte neustarten und zweistelligen Zahlenwert mit 0<=Stunden<=23 und 0<=Minuten<=59 eingeben!")
    exit(-1)

timeMin = ((x * 60) + y)
timeGE = (timeMin - 420)

if (timeGE > 0):
    print("%02d:%02d" % (timeGE // 60, timeGE % 60))
else:
    timeGE = (1440 + timeGE)
    print("%02d:%02d" % (timeGE // 60, timeGE % 60))
