"""
Copyright (c) 2019  Luis Michaelis, Philip Laskowicz
Licensed under MIT (https://opensource.org/licenses/mit-license.php).
"""


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
    def __init__(self, name, weiblich):
        super().__init__(name, weiblich)
        self.wildschweine_gegessen = 0

        if weiblich and not name.endswith('ine'):
            self.name = name + 'ine'
        elif not weiblich and not name.endswith('ix'):
            self.name = name + 'ix'

    def set_name(self, neuername):
        self.name = neuername

        if self.weiblich and not self.name.endswith('ine'):
            self.name = neuername + 'ine'
        elif not self.weiblich and not self.name.endswith('ix'):
            self.name = neuername + 'ix'

    def get_wildschweine(self):
        return self.wildschweine_gegessen

    def iss_wildschwein(self):
        self.wildschweine_gegessen += 1


class Roemer(Mensch):
    imperator = None

    def __init__(self, name, weiblich):
        super().__init__(name, weiblich)
        self.verloren = 0

        if weiblich and not name.endswith('a'):
            self.name = name + 'a'
        elif not weiblich and not name.endswith('us'):
            self.name = name + 'us'

        if Roemer.imperator is None:
            Roemer.imperator = self

    def set_name(self, neuername):
        self.name = neuername

        if self.weiblich and not self.name.endswith('a'):
            self.name = neuername + 'a'
        elif not self.weiblich and not self.name.endswith('us'):
            self.name = neuername + 'us'

    def verliere(self):
        self.verloren += 1

    def wie_oft_verloren(self):
        return self.verloren

    def werde_imperator(self):
        Roemer.imperator = self


class Dorf:
    def __init__(self, bewohner, druide, barde):
        self.bewohner = bewohner
        self.druide = druide
        self.barde = barde

    def set_barde(self, barde):
        self.barde = barde

        if barde not in self.bewohner:
            self.bewohner.add(barde)

    def get_barde(self):
        return self.barde

    def set_druide(self, druide):
        self.druide = druide

        if druide not in self.bewohner:
            self.bewohner.add(druide)

    def get_druide(self):
        return self.druide

    def get_bewohner(self):
        return self.bewohner


class Legion:
    def __init__(self, soldaten, zenturio):
        self.zenturio = zenturio
        self.soldaten = soldaten

    def get_zenturio(self):
        return self.zenturio

    def set_zenturio(self, zenturio):
        self.zenturio = zenturio

    def rekrutiere(self, ein_roemer: Roemer):
        if ein_roemer.weiblich or ein_roemer == self.zenturio:
            return

        self.soldaten.add(ein_roemer)

    def pensioniere(self, ein_roemer):
        if ein_roemer in self.soldaten:
            self.soldaten.remove(ein_roemer)


def wettkampf(ein_dorf: Dorf, eine_legion: Legion):
    gallier = list(ein_dorf.bewohner)
    roemer = list(eine_legion.soldaten)
    roemer.append(eine_legion.zenturio)

    for i in range(max(len(gallier), len(roemer))):
        r = roemer[i % len(roemer)]
        print(
            f'Gallier {gallier[i % len(gallier)].name} misst sich mit {"Roemer" if r != eine_legion.zenturio else "Zenturio"} {r.name}')
        roemer[i % len(roemer)].verliere()

    for g in ein_dorf.bewohner:
        if g != ein_dorf.barde:
            g.iss_wildschwein()


# Nicht veraendern!
if __name__ == '__main__':

    # Loesen Sie Aufgabenteil g) hier:
    Laureline = Gallier('Laurel', True)
    Canine = Gallier('Canine', True)
    Apfelsine = Gallier('Apfelsine', True)

    Praefix = Gallier('Praefix', False)
    Infix = Gallier('Infix', False)
    Postfix = Gallier('Postf', False)

    Salta = Roemer('Salt', True)
    Mendoza = Roemer('Mendoza', True)
    Ushuaia = Roemer('Ushuaia', True)

    Primus = Roemer('Primus', False)
    Secundus = Roemer('Secundus', False)
    Tertius = Roemer('Tertius', False)
    Quartus = Roemer('Quartus', False)
    Quintus = Roemer('Quint', False)

    Oelixdorf = Dorf({Laureline, Apfelsine, Praefix}, Laureline, Praefix)
    Bekdorf = Dorf({Laureline, Postfix, Infix, Canine}, Infix, Canine)
    Hispana = Legion({Quintus, Quartus, Tertius}, Salta)

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
