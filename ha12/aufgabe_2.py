class Vliste:
    def __init__(self, eintrag, nachfolger):
        self._eintrag = eintrag
        self._nachfolger: Vliste = nachfolger

    def gleich(self, other):
        if self._eintrag == other.eintrag:
            if self._nachfolger is not None and other.nachfolger is not None:
                if self._nachfolger.gleich(other.nachfolger):
                    return True
            elif self._nachfolger == other.nachfolger:
                return True
        return False

    def append(self, entry):
        if self._nachfolger is None:
            self._nachfolger = Vliste(entry, None)
        else:
            self._nachfolger.append(entry)

    def extend(self, entry):
        if self._nachfolger is None:
            self._nachfolger = entry
        else:
            self._nachfolger.extend(entry)

    def filter(self, fct):
        if fct(self._eintrag):
            return Vliste(self._eintrag, self._nachfolger.filter(fct)) if self._nachfolger is not None else Vliste(
                self._eintrag, None)
        else:
            return self._nachfolger.filter(fct)

    def map(self, fct):
        return Vliste(fct(self._eintrag), self._nachfolger.map(fct)) if self._nachfolger is not None else Vliste(
            fct(self._eintrag), None)

    def nachListe(self):
        return [self._eintrag] + self._nachfolger.nachListe() if self._nachfolger is not None else [self._eintrag]

    #def debug(self, ret: str = "", depth: int = 0):
    #    depth += 1
    #    if self._nachfolger is None:
    #        return ret + " ( " + str(self._eintrag) + " )" + (depth - 1) * ")"
    #    else:
    #        return self._nachfolger.debug(ret + " ( " + str(self._eintrag), depth)


def nachVliste(list: list):
    return Vliste(list.pop(0), nachVliste(list)) if len(list) > 1 else Vliste(list.pop(0), None)


if __name__ == '__main__':
    testList = Vliste(5, Vliste("ab", Vliste(0.36, None)))
    testList2 = Vliste(5, Vliste("ab", Vliste(0.36, Vliste(True, None))))
    testList3 = Vliste(1, Vliste(2, None))
    testList4 = Vliste(1, Vliste(2, Vliste(3, None)))
    testList5 = Vliste(5, Vliste("ab", Vliste(0.36, None)))
    testList6 = Vliste(5, Vliste("ab", Vliste(0.36, None)))
    testList7 = nachVliste([3, 2, 1])
    testList6.extend(Vliste(True, None))
    testList3.append(3)
    print(testList.nachfolger.nachfolger.eintrag)
    print(testList2.gleich(testList6))
    print(testList.gleich(testList5))
    print(testList3.gleich(testList4))
    print(testList2.nachListe())
    print(Vliste(1, Vliste(2, Vliste(3, None))).filter(lambda x: x % 2 == 1).debug())
    print(Vliste(1, Vliste(2, Vliste(3, None))).map(lambda x: x + 2).debug())
    #print(testList.debug(), testList2.debug(), testList3.debug(), testList4.debug(), testList5.debug(), testList6.debug(), testList7.debug(), sep="\n")
