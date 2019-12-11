def zyklisch(wb, i):
    assert type(wb) == dict, 'erster Parameter kein Woerterbuch'
    assert type(i) == int, 'zweiter Parameter kein Integer'
    assert type(x for x in wb) == int and type(wb[y] for y in wb) == int, 'erster Parameter kein int - int Woerterbuch'
    assert i in wb, 'zweiter Parameter kein Schlussel des ersten Parameters'
    return False if i not in wb else zyklisch(wb,wb[i])

if __name__ == "__main__":
    pass
