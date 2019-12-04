import random


def init(x: int) -> tuple:
    tpl: tuple = ()

    for i in range(x):
        tpl[i] = random.randint(1, x)

    return tpl


def strategie(spielstand: tuple, wb: dict = {}):
    for i in range(len(spielstand)):
        uebrig = spielstand[i]

        if uebrig in wb:
            return -1 if wb[uebrig] == -1 else i, wb[uebrig]

        if uebrig == 1:
            wb[uebrig] = -1
        elif 2 <= uebrig and uebrig <= 4:
            wb[uebrig] = uebrig - 1
            return i, uebrig - 1
        else:
            spielstandLst = list(spielstand)

            for j in range(1, 4):
                spielstandLst[i] = uebrig - j

                if strategie(tuple(spielstandLst), wb) == -1:
                    wb[uebrig] = j
                    return i, j

    return -1
