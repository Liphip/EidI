class Vliste:
    def __init__(self, eintrag, nachfolger):
        self.eintrag = eintrag
        self.nachfolger = nachfolger

    def append(self, eintrag):
        x = self

        while x.nachfolger is not None:
            x = x.nachfolger

        x.nachfolger = Vliste(eintrag, None)

    def extend(self, liste):
        x = self

        while x.nachfolger is not None:
            x = x.nachfolger

        x.nachfolger = liste

    def filter(self, func):
        a, b = self, None

        while True:
            if func(a.eintrag):
                if b is None:
                    b = Vliste(a.eintrag, None)
                else:
                    b.append(a.eintrag)

            a = a.nachfolger

            if a is None:
                return b

    def map(self, func):
        a, b = self, None

        while True:
            if b is None:
                b = Vliste(func(a.eintrag), None)
            else:
                b.append(func(a.eintrag))

            a = a.nachfolger

            if a is None:
                return b

    def nachListe(self):
        a, l = self, []

        while True:
            l.append(a.eintrag)
            a = a.nachfolger

            if a is None:
                return l

    def gleich(self, other):
        a, b = self, other
        while True:
            if a.eintrag == b.eintrag and a.eintrag is None:
                return True
            elif a.eintrag != b.eintrag:
                return False

            a = a.nachfolger
            b = b.nachfolger



if __name__ == '__main__':
    # a)
    liste = Vliste(
        5,
        Vliste(
            "ab",
            Vliste(
                0.36,
                None
            )
        )
    )

    print(liste.nachfolger.nachfolger.eintrag)

    ##########################
    a = Vliste(
        1,
        Vliste(
            2,
            Vliste(
                3,
                None
            )
        )
    )
    print(a.nachListe())

    a.append(4)
    print(a.nachListe())

    a.extend(Vliste(5, Vliste(6, None)))
    print(a.nachListe())

    a = a.filter(lambda x: x <= 4)
    print(a.nachListe())

    a = a.map(lambda x: x * 2)
    print(a.nachListe())
