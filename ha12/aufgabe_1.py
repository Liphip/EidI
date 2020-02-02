import random


class Mensch(object):
    def __init__(self, name, weiblich):
        self.name = name
        self.weiblich = weiblich

    def get_name(self):
        return self.name

    def get_weiblich(self):
        return self.weiblich

    def set_name(self, neuername):
        self.name = neuername


class Gallier(Mensch):
    def __init__(self, wildschweine, name, weiblich):
        super().__init__(name, weiblich)
        self._wildschweine = wildschweine
        if (self.name[-3:0] != "ine" and weiblich) or (self.name[-2:0] != "ix" and not weiblich):
            self.name += "ine" if weiblich else "ix"

    def set_name(self, neuername):
        if (self.name[-3:0] != "ine" and self.get_weiblich()) or (self.name[-2:0] != "ix" and not self.get_weiblich()):
            self.name += "ine" if self.get_weiblich() else "ix"

    def get_wildschweine(self):
        return self._wildschweine

    def iss_wildschweine(self):
        self._wildschweine += 1


class Roemer(Mensch):
    imperator = None

    def __init__(self, looses, name, weiblich):
        super().__init__(name, weiblich)
        self.looses = looses
        if (self.name[-1:0] != "a" and weiblich) or (self.name[-2:0] != "us" and not weiblich):
            self.name += "a" if weiblich else "us"
        if Roemer.imperator is None:
            Roemer.imperator = self

    def set_name(self, neuername):
        if (self.name[-1:0] != "a" and self.get_weiblich()) or (self.name[-2:0] != "us" and not self.get_weiblich()):
            self.name += "a" if self.get_weiblich() else "us"

    def verliere(self):
        self.looses += 1

    def wie_oft_verloren(self):
        return self.looses

    def werde_imperator(self):
        Roemer.imperator = self


class Dorf:
    def __init__(self, bewohner: set, druide: Gallier, barde: Gallier):
        self.bewohner: set = bewohner
        self.druide = druide
        self.barde = barde
        if self.druide not in self.bewohner:
            self.bewohner.add(druide)
        if self.druide not in self.bewohner:
            self.bewohner.add(druide)

    def get_druide(self):
        return self.druide

    def get_barde(self):
        return self.barde

    def get_bewohner(self):
        return self.bewohner

    def set_druide(self, druide: Gallier):
        self.druide = druide
        if druide not in self.bewohner:
            self.bewohner.add(druide)

    def set_barde(self, barde: Gallier):
        self.barde = barde
        if barde not in self.bewohner:
            self.bewohner.add(barde)


class Legion:
    def __init__(self, soldaten: set, zenturio: Roemer):
        self.soldaten: set = soldaten
        self.zenturio = zenturio

    def get_zenturio(self):
        return self.zenturio

    def get_soldaten(self):
        return self.soldaten

    def set_zenturio(self, zenturio: Roemer):
        self.zenturio = zenturio

    def rekrutiere(self, ein_roemer: Roemer):
        if ein_roemer.get_weiblich() == False and not ein_roemer in self.soldaten and not ein_roemer is self.zenturio:
            self.soldaten.add(ein_roemer)

    def pensioniere(self, ein_roemer: Roemer):
        if ein_roemer in self.soldaten:
            self.soldaten.remove(ein_roemer)


def wettkampf(ein_dorf: Dorf, eine_legion: Legion):
    if len(ein_dorf.bewohner) == len(eine_legion.soldaten):
        iGallier = 0
        for iRoemer in len(eine_legion.get_soldaten()):
            if iGallier >= len(ein_dorf.get_bewohner()) - 1:
                print("Gallier " + ein_dorf.get_bewohner()[
                    random.randint(0, len(ein_dorf.get_bewohner()))].get_name() + " misst sich mit Roemer " +
                      eine_legion.get_soldaten()[iRoemer].get_name())
            else:
                print("Gallier " + ein_dorf.get_bewohner()[iGallier].get_name() + " misst sich mit Roemer " +
                      eine_legion.get_soldaten()[iRoemer].get_name())
                iGallier += 1

    print(
        "Gallier " + ein_dorf.get_barde().get_name() + " misst sich mit Roemer " + eine_legion.get_zenturio().get_name())

    for gallier in ein_dorf.bewohner:
        gallier.iss_wildschweine()
    ein_dorf.druide.iss_wildschweine()


# Nicht veraendern!
if __name__ == '__main__':

    # Loesen Sie Aufgabenteil g) hier:

    Laureline, Canine, Apfelsine = Gallier(0, "Laurel", True), Gallier(0, "Canine", True), Gallier(0, "Apfelsine", True)
    Praefix, Infix, Postfix = Gallier(0, "Praefix", False), Gallier(0, "Infix", False), Gallier(0, "Postf", False)
    Salta, Mendoza, Ushuaia = Roemer(0, "Salt", True), Roemer(0, "Mendoza", True), Roemer(0, "Ushuaia", True)
    Primus, Secundus, Tertius, Quartus, Quintus = Roemer(0, "Primus", False), Roemer(0, "Secundus", False), Roemer(0, "Tertius", False), Roemer(0, "Quartus", False), Roemer(0, "Quint", False)
    Oelixdorf, Bekdorf = Dorf({Laureline, Apfelsine, Praefix}, Laureline, Praefix), Dorf({Laureline, Postfix, Infix}, Infix, Canine)
    Hispana = Legion({Quintus, Quartus, Tertius, Mendoza}, Salta)

    # Diesen Teil duerfen Sie nicht veraendern

    if not (Laureline.get_name() == "Laureline" and Canine.get_name() == "Canine"):
        print("Fehler: Gallierinnen falsch benannt")

    if not (Praefix.get_name() == "Praefix" and Postfix.get_name() == "Postfix"):
        print("Fehler: Gallier falsch benannt")

    if not (Salta.get_name() == "Salta" and Ushuaia.get_name() == "Ushuaia"):
        print("Fehler: Roemerinnen falsch benannt")

    if not (Primus.get_name() == "Primus" and Quintus.get_name() == "Quintus"):
        print("Fehler: Roemer falsch benannt")

    if not (Roemer.imperator == Salta):
        print("Fehler: Imperator falsch")

    Primus.werde_imperator()

    if not Roemer.imperator == Primus:
        print("Fehler: Thronfolge kaputt")

    Laureline.set_name("Geraldine")
    Canine.set_name("Paul")
    Praefix.set_name("Unix")
    Infix.set_name("Append")
    Mendoza.set_name("Catamarca")
    Ushuaia.set_name("Viedm")
    Primus.set_name("Airbus")
    Secundus.set_name("Autob")

    if not (
            Laureline.get_name() == "Geraldine" and Canine.get_name() == "Pauline" and Praefix.get_name() == "Unix" and Infix.get_name() == "Appendix" and Mendoza.get_name() == "Catamarca" and Ushuaia.get_name() == "Viedma" and Primus.get_name() == "Airbus" and Secundus.get_name() == "Autobus"):
        print("Fehler: Namensaenderung funktioniert nicht korrekt")

    Laureline.set_name("Laureline")
    Canine.set_name("Canine")
    Praefix.set_name("Praefix")
    Infix.set_name("Infix")
    Mendoza.set_name("Mendoza")
    Ushuaia.set_name("Ushuaia")
    Primus.set_name("Primus")
    Secundus.set_name("Secundus")

    if not (Oelixdorf.get_barde() == Praefix and Oelixdorf.get_druide() == Laureline and Oelixdorf.get_bewohner() == {
        Apfelsine, Praefix, Laureline}):
        print("Fehler: Dorf falsch erstellt")

    if not (Bekdorf.get_barde() == Canine and Bekdorf.get_druide() == Infix and Bekdorf.get_bewohner() == {Laureline,
                                                                                                           Postfix,
                                                                                                           Infix,
                                                                                                           Canine}):
        print("Fehler: Dorf falsch erstellt")

    if not (Hispana.get_zenturio() == Salta and Hispana.soldaten == {Quintus, Quartus, Tertius}):
        print("Fehler: Legion falsch")

    Hispana.rekrutiere(Secundus)
    Hispana.rekrutiere(Ushuaia)
    Hispana.pensioniere(Tertius)
    Hispana.pensioniere(Tertius)
    Hispana.rekrutiere(Salta)

    if not (Hispana.soldaten == {Secundus, Quartus, Quintus}):
        print("Fehler: Legion arbeitet falsch")

    wettkampf(Oelixdorf, Hispana)

    if not ((Secundus.wie_oft_verloren() == 1) and (Salta.wie_oft_verloren() == 1) and (
            Laureline.get_wildschweine() == 1) and (Canine.get_wildschweine() == 0)):
        print("Fehler: Wettkampf funktioniert nicht")

    Bekdorf.set_barde(Laureline)
    Hispana.rekrutiere(Primus)
    wettkampf(Bekdorf, Hispana)
    if not (
            Secundus.wie_oft_verloren() == 2 and Primus.wie_oft_verloren() == 1 and Laureline.get_wildschweine() == 1 and Canine.get_wildschweine() == 1):
        print("Fehler: Wettkampf funktioniert nicht richtig")

# Ihre Ausgabe soll in etwa folgendes Format haben:
# Gallier Apfelsine misst sich mit Roemer Quintus.
# Gallier Praefix misst sich mit Roemer Quartus.
# Gallier Apfelsine misst sich mit Roemer Secundus.
# Gallier Praefix misst sich mit Zenturio Salta.
# Gallier Laureline misst sich mit Roemer Primus.
# Gallier Postfix misst sich mit Roemer Secundus.
# Gallier Canine misst sich mit Roemer Quartus.
# Gallier Laureline misst sich mit Roemer Quintus.
# Gallier Postfix misst sich mit Zenturio Salta.
