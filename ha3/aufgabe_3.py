def lies_zeile(string: str) -> tuple:
    if string.count(',') != 2:
        exit('Formatfehler: Keine 2 Kommas in Zeile Gefunden.')
    
    return tuple(string.split(','))


def lies_datei(handle) -> list:
    return [lies_zeile(i.replace('\n', '')) for i in handle.readlines()]


def hat_schauspieler(data: list, name: str) -> bool:
    for i in data:
        if name in i:
            return True
    
    return False


def schauspieler_zusammenarbeit(data: list, name: str) -> list:
    actors = []
    
    for i in data:
        index = i.index(name) if name in i else -1
        
        if index == -1:
            continue

        n = i[1 if index == 2 else 2]
        
        if n not in actors:
            actors.append(n)

    return actors


def fuege_ein(data: list, insert: tuple):
    data = data[:]  # Copy the list
    
    for i in range(len(data)):
        if data[i][2] == insert[2]:
            data.insert(i, insert)
            break
            
    return data
