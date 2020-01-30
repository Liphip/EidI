# Aufgabe 2
#
import math
import sys
import random
import time

# Sortiert Liste liste mittels Insertionsort
# Function to do insertion sort 
def inssort(L): 
    global vergleiche
    arr=L[:]
    # Traverse through 1 to len(arr) 
    for i in range(1, len(arr)): 
  
        key = arr[i] 
  
        # Move elements of arr[0..i-1], that are 
        # greater than key, to one position ahead 
        # of their current position 
        j = i-1
        while j >= 0 and key < arr[j] : 
            vergleiche += 1
            arr[j + 1] = arr[j] 
            j -= 1
        vergleiche += 1
        arr[j + 1] = key 
    return arr



# mische aufsteigend sortierte Listen links und rechts zu einer aufsteigend sortierten TODOiste
def merge(links, rechts):
	global vergleiche
	resultat = []
	i,j = 0,0

	while i < len(links) and j < len(rechts):
		vergleiche += 1
		if links[i] < rechts[j]:
			resultat.append(links[i])
			i += 1
		else:
			resultat.append(rechts[j])
			j += 1

	while i < len(links):
		resultat.append(links[i])
		i+= 1

	while j < len(rechts):
		resultat.append(rechts[j])
		j += 1

	return resultat

# Sortiert Liste liste mittels Mergesort
def mergesort(liste):
	if len(liste) < 2:
		return liste
	
	mitte = len(liste) // 2
	links = mergesort(liste[:mitte])
	rechts = mergesort(liste[mitte:])
	return merge(links,rechts)

# Sortiere Liste liste mittels Quicksort
def qsort(liste):  
	global vergleiche
	linke=[]
	rechte=[]
	if len(liste) <= 1:
		return liste

	pivot = 0 # Pivotwahl

	for i in range(len(liste)):
		if i!= pivot:
			vergleiche += 1
			if liste[i] < liste[pivot]:
				linke.append(liste[i])
			else:
				rechte.append(liste[i])

	return qsort(linke)+liste[pivot:pivot+1]+qsort(rechte)


# Sortiere Liste  liste mittels Quicksort
def qsort_ma3(liste):  
    global vergleiche
    return liste
	

def qsort_cutoff(liste):  
    global vergleiche
    return liste

def qsort_intro(liste):
    global vergleiche
    return liste


def qsort_cutoff_ma3(liste):
    global vergleiche
    return liste

def qsort_random(liste):
    global vergleiche
    return liste
	
def teste(liste, funktion):
	global vergleiche
	L = liste[0][:]
	vergleiche = 0
	t0 = time.process_time()
	L1 = funktion[0](L)
	t1 = time.process_time() - t0
	L2 = sorted(L1)
	if L2 != L1:
		print(f"Funktion {funktion[1]} sortiert nicht richtig")
	
	print(f"{funktion[1]}:  Zeit: {str(t1)[:5]} Sekunden, Vergleiche: {vergleiche} ")

# Nicht veraendern!
if __name__ == '__main__':
# Ihren globalen Testcode koennen Sie hier platzieren:

	


	sys.setrecursionlimit(20000)
	n = 5000

	listen = [ ([i for i in range(n)], "Aufsteigende Liste" ), ([ n-i for i in range(n) ],"Absteigende Liste" ),] + [  (random.sample(range(n),n), str(i)+"-te zufaellige Liste")   for i in range(5)  ]
	funktionen = [(inssort, "Insertionsort"+" "*11), (mergesort, "Mergesort"+" "*15), (qsort,"Quicksort" + " "*15), (qsort_intro,"Introsort" + " " *15), (qsort_cutoff,"Quicksort mit Cutoff"+ " "*4), (qsort_ma3,"Quicksort mit Ma3"+" "*7 ), (qsort_cutoff_ma3, "Quicksort mit Cutoff/Ma3"), (qsort_random, "Quicksort mit zuf. Pivot")]
	for liste in listen:
		print(f"Teste nun diese Liste: {liste[1]}")
		for funktion in funktionen:	
			teste(liste, funktion) 
		print("\n")
		
		




