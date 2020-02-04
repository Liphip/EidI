class Vliste:
    def __init__(self, eintrag, nachfolger):
        self.eintrag = eintrag
        self.nachfolger: Vliste = nachfolger

    def gleich(self, other):
        if self.eintrag == other.eintrag:
            if self.nachfolger is not None and other.nachfolger is not None:
                if self.nachfolger.gleich(other.nachfolger):
                    return True
                elif self.nachfolger == other.nachfolger:
                    return True
        return False

    def append(self, entry):
        if self.nachfolger == None:
            self.nachfolger = Vliste(entry, None)
        else:
            self.nachfolger.append(entry)


if __name__ == '__main__':
    testList = Vliste(5, Vliste("ab", Vliste(0.36, None)))
    testList2 = Vliste(5, Vliste("ab", Vliste(0.36, Vliste(True, None))))
    testList3 = Vliste(1, Vliste(2, None))
    testList4 = Vliste(1, Vliste(2, Vliste(3, None)))
    testList3.append(3)
    print(testList.nachfolger.nachfolger.eintrag)
    print(testList.gleich(testList))
    print(testList3.gleich(testList4))
