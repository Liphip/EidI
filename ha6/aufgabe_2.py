import random


def init(x):
    return tuple([random.randint(1, x + 1) for _ in range(7)])


def strategie(spielstand, wb={}):
    for i in range(len(spielstand)):
        v = spielstand[i]
        
        if v in wb and wb[v] != -1:
            return i, wb[v]
        elif v == 1:
            wb[v] = -1
        elif 2 <= v <= 4:
            wb[v] = v - 1
            return i, v - 1
        else:
            s = list(spielstand)
            
            for r in range(1, 4):
                s[i] = v - r
                
                if strategie(tuple(s), wb) == -1:
                    wb[v] = r
                    return i, r
    
    return -1
