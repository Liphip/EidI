import logging
import random
import time
import sys


# Sie duerfen diese Funktion nicht veraendern.
def sortiere(kleiner, L):
    trenner = 0
    while trenner != len(L):
        for i in range(trenner, len(L)):
            if kleiner(L[i], L[trenner]):
                L[trenner], L[i] = L[i], L[trenner]
        trenner += 1
    return L


# Sie duerfen diese Funktion nicht veraendern.
def ausgabe(stand):
    for i in range(9):
        tmp = ""
        if i == 3 or i == 6:
            print("-" * 30)
        for j in range(9):
            if j == 3 or j == 6:
                tmp += "   |  "
            d = stand[(i, j)]
            if len(d) == 1:
                for e in d:
                    tmp += " " + str(e)
            else:
                tmp += " " + "*"
        print(tmp)


# Sie duerfen diese Funktion nicht veraendern.
def kopie(stand):
    return {(i, j): stand[(i, j)].copy() for i in range(9) for j in range(9)}


# Sie duerfen diese Funktion nicht veraendern.
def buersten(sudoku):
    def abhaengig(i, j, x, y):
        return (not ((i == x) and (j == y))) and ((i == x) or (j == y) or (i // 3 == x // 3) and (j // 3 == y // 3))

    sudokuk = kopie(sudoku)
    entfernt = False
    effects = [(wert, x, y) for i in range(9) for j in range(9) for x in range(9) for y in range(9) \
               for wert in sudokuk[(i, j)] if
               len(sudokuk[(i, j)]) == 1 and wert in sudokuk[(x, y)] and abhaengig(i, j, x, y)]
    for (wert, x, y) in effects:
        if wert in sudokuk[(x, y)]:
            sudokuk[(x, y)].remove(wert)
            entfernt = True
    if entfernt:
        sudokuk = buersten(sudokuk)
    return sudokuk


# Sie duerfen diese Funktion nicht veraendern.
def erfuellbar(stand):
    if len([stand[(i, j)] for i in range(9) for j in range(9) if len(stand[(i, j)]) == 0]) >= 1:
        return False
    elif len([stand[(i, j)] for i in range(9) for j in range(9) if len(stand[(i, j)]) == 1]) == 81:
        print("Wir haben eine Loesung gefunden")
        ausgabe(stand)
        return True
    else:
        nonsingletons = [(i, j, stand[(i, j)]) for i in range(9) for j in range(9) if len(stand[(i, j)]) > 1]
        cmp = lambda a, b: len(a[2]) > len(b[2])
        nonsingletons = sortiere(cmp, nonsingletons)
        (i, j, ziffern) = nonsingletons.pop()
        ziffernkopie = ziffern.copy()
        old = stand.copy()
        for x in ziffernkopie:
            stand[(i, j)].clear()
            stand[(i, j)].add(x)
            stand = buersten(stand)
            if erfuellbar(stand):
                return True
            stand = old.copy()
        return False


# Sie duerfen diese Funktion veraendern. Kennzeichnen Sie geaenderte Zeilen mit einem Kommentar. Beachten Sie, dass die Funktionen einen int zurueck geben soll, und dass der rekursive Aufruf noch die Funktion erfuellbar aufruft!
def wieviele(stand):  # geaendert
    if len([stand[(i, j)] for i in range(9) for j in range(9) if len(stand[(i, j)]) == 0]) >= 1:
        return 0  # geaendert
    elif len([stand[(i, j)] for i in range(9) for j in range(9) if len(stand[(i, j)]) == 1]) == 81:
        # ausgabe(stand)
        return 1  # geaendert
    else:
        possibilities = 0  # geaendert
        nonsingletons = [(i, j, stand[(i, j)]) for i in range(9) for j in range(9) if len(stand[(i, j)]) > 1]
        cmp = lambda a, b: len(a[2]) > len(b[2])
        nonsingletons = sortiere(cmp, nonsingletons)
        (i, j, ziffern) = nonsingletons.pop()
        ziffernkopie = ziffern.copy()
        old = stand.copy()
        for x in ziffernkopie:
            if possibilities >= 2:  # geaendert
                return 2  # geaendert
            stand[(i, j)].clear()
            stand[(i, j)].add(x)
            stand = buersten(stand)
            if erfuellbar(stand):  # geaendert
                possibilities += 1  # geaendert
            stand = old.copy()
        return possibilities  # geaendert


# Sternchenaufgabe. Sie duerfen diese Funktion veraendern.
def generiere(stand, first=True):
    logging.debug("Starting 'generiere'")

    def possible(stand) -> bool:
        logging.debug("Starting 'possible'")
        # print("Testing...")
        for i in stand:
            # print(i, stand[i])
            if stand[i] != {1, 2, 3, 4, 5, 6, 7, 8, 9}:
                # print("Valid")
                logging.info("Finished 'possible' with invalid stand")
                return False
        logging.info("Finished 'possible' with valid stand")
        return True

    def setRandomCell(stand):
        logging.debug("Starting 'setRandomCell'")
        tested = []
        standc = stand.copy()
        logging.info("Searching random Cell")
        startTime = time.time_ns()
        randCell = (random.randint(0, 8), random.randint(0, 8))
        while not len(stand[randCell]) == 9 or randCell in tested and len(tested) < 80:
            # test = randCell in tested
            # print("Searching...", randCell, stand[randCell], len(stand[randCell]), test)
            randCell = (random.randint(0, 8), random.randint(0, 8))
            if not randCell in tested:
                tested.append(randCell)
        if len(tested) >= 80:
            logging.fatal("Can't find new random Cell")
            logging.fatal("Terminating Process with code -1")
            exit(-1)
        logging.debug("Found random Cell in " + str(time.time_ns() - startTime) + "ns")
        standc[randCell] = {random.randint(1, 9)}
        logging.debug("Finished 'setRandomCell' with new stand")
        return standc

    logging.info("Validating stand")
    if first:
        if not possible(stand):
            # print("Invalid")
            return stand

    # print("Setting random Cell...")
    standc = setRandomCell(stand)
    # print("Random Cell set")

    logging.debug("Testing possibilities")
    logging.debug("Starting 'wieviele'")
    possibilities = wieviele(standc)
    logging.info("Finished 'wieviele' with result " + str(possibilities))
    if possibilities < 1:
        # print("1")
        logging.info("Possibilities to low -> restarting 'generiere' recursive with original stand")
        return generiere(stand, False)
    elif possibilities > 1:
        # print("2")
        logging.info("Possibilities to high -> restarting 'generiere' recursive with new stand")
        return generiere(standc, False)
    else:
        # print("3")
        logging.info("Finished 'generiere' with valid Stand")
        return standc


# print(standc)
# print()
# return generiere(stand) if wieviele(standc) < 1 else generiere(standc) if wieviele(standc) > 1 else standc


# Initialisierungen fuer Sudokus.

# Sie duerfen diese Funktion nicht veraendern.
def init1():
    stand[(0, 0)] = {8}
    stand[(1, 2)] = {3}
    stand[(1, 3)] = {6}
    stand[(2, 1)] = {7}
    stand[(2, 4)] = {9}
    stand[(2, 6)] = {2}
    stand[(3, 1)] = {5}
    stand[(3, 5)] = {7}
    stand[(4, 4)] = {4}
    stand[(4, 5)] = {5}
    stand[(4, 6)] = {7}
    stand[(5, 3)] = {1}
    stand[(5, 7)] = {3}
    stand[(6, 2)] = {1}
    stand[(6, 7)] = {6}
    stand[(6, 8)] = {8}
    stand[(7, 2)] = {8}
    stand[(7, 3)] = {5}
    stand[(7, 7)] = {1}
    stand[(8, 1)] = {9}
    stand[(8, 6)] = {4}


# Sie duerfen diese Funktion nicht veraendern.
def init2():
    # b={(i,j):{} for i in range(9) for j in range(9)}
    stand[(0, 1)] = {6}
    stand[(0, 3)] = {1}
    stand[(0, 5)] = {4}
    stand[(0, 7)] = {5}

    stand[(1, 2)] = {8}
    stand[(1, 3)] = {3}
    stand[(1, 5)] = {5}
    stand[(1, 6)] = {6}

    stand[(2, 0)] = {2}
    stand[(2, 8)] = {1}

    stand[(3, 0)] = {8}
    stand[(3, 3)] = {4}
    stand[(3, 5)] = {7}
    stand[(3, 8)] = {6}

    stand[(4, 2)] = {6}
    stand[(4, 6)] = {3}

    stand[(5, 0)] = {7}
    stand[(5, 3)] = {9}
    stand[(5, 5)] = {1}
    stand[(5, 8)] = {4}

    stand[(6, 0)] = {5}
    stand[(6, 8)] = {2}

    stand[(7, 2)] = {7}
    stand[(7, 3)] = {2}
    stand[(7, 5)] = {6}
    stand[(7, 6)] = {9}

    stand[(8, 1)] = {4}
    stand[(8, 3)] = {5}
    stand[(8, 5)] = {8}
    stand[(8, 7)] = {7}


# Sie duerfen diese Funktion nicht veraendern.
def init3():
    stand[(0, 8)] = {4}

    stand[(1, 0)] = {6}
    stand[(1, 2)] = {2}

    stand[(2, 3)] = {3}
    stand[(2, 4)] = {1}
    stand[(2, 5)] = {9}

    stand[(3, 1)] = {1}
    stand[(3, 2)] = {3}
    stand[(3, 4)] = {2}

    # stand[(4,1)]={9}
    stand[(4, 3)] = {8}
    stand[(4, 6)] = {5}

    # stand[(5,1)]={7}
    stand[(5, 6)] = {3}

    # stand[(6,0)]={4}


if __name__ == "__main__":
    logging.basicConfig(filename='log.txt', level=logging.DEBUG, format='[%(asctime)s] %(levelname)s:%(message)s',
                        datefmt='%I:%M:%S', filemode='w')

    logging.debug("Started")
    # print(sys.getrecursionlimit())
    # sys.setrecursionlimit(10000)
    # print(sys.getrecursionlimit())

    stand = {(i, j): set(range(1, 10)) for i in range(9) for j in range(9)}
    logging.info("Stand set to: " + str(stand))
    # print(stand)
    # stand[(6, 7)] = {6}

    # stand[(7, 3)] = {7}
    # stand[(7, 5)] = {3}
    # stand[(7, 7)] = {9}
    ausgabe(generiere(stand))

    # stand[(8, 3)] = {9}
    # stand[(8, 5)] = {6}
    # stand[(8, 7)] = {8}
    logging.debug("Starting 'init'")
    init1()
    logging.info("Init finished -> stand set to: " + str(stand))

    # print("Wir wollen folgendes Sudoku loesen")
    # ausgabe(stand)
    # print("Ausgegeben!")
    # erfuellbar(stand)
    # print("Fertig!")
    logging.debug("Starting 'wieviele'")
    print(wieviele(stand))
    logging.debug("Finished 'wieviele'")
    logging.debug("Finished Process with code 0")
    exit(0)
