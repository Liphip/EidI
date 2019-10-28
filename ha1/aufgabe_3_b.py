x = int(input("Geben sie die Stunden ihrer geschätzten Ankuftszeit an > "))
y = int(input("Geben sie die Minuten ihrer geschätzten Ankuftszeit an > "))

timeGE = (((x * 60) + y) - (7*60))
timeGE %= 24 * 60
print("%02d:%02d" % (timeGE // 60, timeGE % 60))
