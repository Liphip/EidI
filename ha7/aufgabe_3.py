def Euklid(a,b):
    assert a>0 and b>0, 'Parameter müssen beide positiv sein'
    return Euklid(b,a) if a<b else b if not a%b else Euklid(b,a%b)


def istBruch(x):
    return type(x[0]) == int and type(x[1]) == int and x[1] > 0

def kuerze(x):
    assert istBruch(x), 'Leider handelt es sich um keinen Bruch'
    return (n/Euklid(i for i in x)for n in x) if x != (0,1) or not (x[0] != 0 and Euklid(abs(x[0]),x[1]) == 1) else x

def plus(x,y):
    assert istBruch(x) and istBruch(y), 'Leider handelt es sich nicht um zwei Bruche'
    return kuerze((((x[0]*y[1])+(y[0]*x[1])),x[1]*y[1]))

def minus(x,y):
    assert istBruch(x) and istBruch(y), 'Leider handelt es sich nicht um zwei Bruche'
    return kuerze((((x[0]*y[1])-(y[0]*x[1])),x[1]*y[1]))

def mal(x,y):
    assert istBruch(x) and istBruch(y), 'Leider handelt es sich nicht um zwei Bruche'
    return kuerze((x[0]*y[0],x[1]*y[1]))

def teile(x,y):
    assert istBruch(x) and istBruch(y), 'Leider handelt es sich nicht um zwei Bruche'
    return kuerze((x[0]*y[1],x[1]*y[0]))


if __name__ == "__main__":
    pass


