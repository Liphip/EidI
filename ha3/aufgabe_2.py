def readLines(line):
    lineT = line.split(',')
    if len(lineT) == 2:
        return lineT
    print('Bitte auf korrekte Formatierung achten!')
    exit(-1)


def readFile(file):
    f = open(file, 'r')
    fLin = f.readlines()
    fL = []
    for i in range(len(fLin)):
        fL += readLines(fLin[i])
    return fL


def cast(list, castin):
    for i in range(len(list)):
        film = list[i]
        if film[1] == castin:
            return True
    return False


def cooperations(list, castin):
    coop = []
    for i in range(len(list)):
        film = list[i]
        if film[1] == castin:
            for j in range(len(list)):
                filmco = list[j]
                if filmco[0] == film[0]:
                    coop += filmco[1]
    return coop


def addIn(list, film):
    reglist = []
    for i in range(len(list)):
        entry = list[i]
        reglist += entry[2]
    reglist += film[2]
    reglist.sort()
    for i in range(len(reglist)):
        if reglist[i] == film[2]:
            list = list[:i] + film + list[i::]
    return list