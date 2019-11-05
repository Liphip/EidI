x = int(input("Geben sie die Stunden ihrer geschätzten Ankuftszeit an > "))
y = int(input("Geben sie die Minuten ihrer geschätzten Ankuftszeit an > "))
print("%02d:%02d" % (((((x * 60) + y) - (7*60)) % (24 * 60)) // 60, ((((x * 60) + y) - (7*60)) % (24 * 60)) % 60))
