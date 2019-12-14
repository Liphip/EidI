def filter_palindrom(liste):
    return filter(lambda x: x != x[::-1], liste)


def liste_kleiner(liste1, liste2):
    return [min(liste1[i], liste2[i]) for i in range(len(liste1))]


def custom_op(liste):
    return liste * 2 if type(liste) == int else liste[::-1] if type(liste) == str else liste


kleiner = lambda x, y: x < y if len(x) == len(y) else len(x) < len(y)


def sortiere(kleiner,L):
    trenner = 0
    while trenner != len(L):
        for i in range(trenner,len(L)):
            if kleiner(L[i],L[trenner]):
                L[trenner], L[i] = L[i], L[trenner]
        trenner += 1
    return L

if __name__ == "__main__":
    pass
    print(sortiere(kleiner,["z","aaa","1","11111","ccv","22"]))
