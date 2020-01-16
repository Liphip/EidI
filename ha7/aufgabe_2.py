"""
Copyright (c) 2019  Luis Michaelis, Philip Laskowicz
Licensed under MIT (https://opensource.org/licenses/mit-license.php).
"""


def zyklisch(wb, i):
    assert type(wb) == dict, 'erster Parameter kein Woerterbuch'
    assert type(i) == int, 'zweiter Parameter kein Integer'
    assert type(x for x in wb) == int and type(wb[y] for y in wb) == int, 'erster Parameter kein int - int Woerterbuch'
    assert i in wb, 'zweiter Parameter kein Schlussel des ersten Parameters'
    
    values = []
    while i not in values:
        values.append(i)
        
        if i in wb:
            i = wb[i]
        else:
            return False
    
    return True


if __name__ == "__main__":
    pass
