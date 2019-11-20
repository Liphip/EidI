"""
Copyright (c) 2019  Luis Michaelis, Philip Laskowicz
Licensed under MIT (https://opensource.org/licenses/mit-license.php).
"""


def intSuperliste(lst: list) -> bool:
    save_type = None
    
    for element in lst:
        if save_type is None:
            save_type = type(element)
        
        if type(element) == list and not intSuperliste(element):
            return False
        elif (type(element) != list and type(element) != int) or type(element) != save_type:
            return False
    
    return True


def Kopie(lst: list) -> list:
    return [(i if type(i) == int else Kopie(i)) for i in lst[:]]
