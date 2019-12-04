import random


def init(x: int) -> tuple:
    tpl: tuple = ()

    for i in range(x):
        tpl[i] = random.randint(1, x)

    return tpl


def strategie(spielstand: tuple, wb: dict = {}):
    def strategie_memoization(uebrig: int, wb: dict = wb):
        if uebrig in wb:
            return wb[uebrig]
        if uebrig == 1:
            wb[uebrig] = -1
            return -1
        if 2 <= uebrig and uebrig <= 4:
            wb[uebrig] = uebrig - 1
            return uebrig - 1
        else:
            for weniger in range(1, 4):
                if strategie_memoization(uebrig - weniger, wb) == -1:
                    wb[uebrig] = weniger
                    return weniger
            return -1
    for i in range(len(spielstand)):
        if spielstand[i] == 1:

    return
