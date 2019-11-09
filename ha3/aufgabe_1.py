def cubicroot(cubicin, e):
    if cubicin < 0:
        cubic = cubicin * -1
    else:
        cubic = cubicin
    root = cubic / 10
    diff = (root ** 3) - cubic
    i = 0
    print(root, diff, cubic)
    while abs(diff) > e and i < 10:
        root = (root + cubic / root) / 2
        diff = (root ** 3) - cubic
        print(root, diff, cubic,cubic / root)
        i += 1

    if cubicin < 0:
        return root * -1
    else:
        return root


if __name__ == '__main__':
    cubic = input('Bitte geben sie die Zahl an, von der sie cubicwurzel ermitteln wollen >>>')
    e = input('Bitte geben sie die gewünschte maximale Abweichung an >>>')
    try:
        float(e)
    except ValueError:
        print('e muss eine Zahl sein.')
        exit(-1)
    if cubic.isnumeric() and float(e) > 0:
        print(cubicroot(float(cubic), float(e)))
    else:
        print(cubic.isnumeric(), e.isnumeric())
        print(cubic + ' oder ' + e + ' liegen nicht im angegebenen Deffinitionsbereich.')
        exit(-1)
