"""
Copyright (c) 2019  Luis Michaelis, Philip Laskowicz
Licensed under MIT (https://opensource.org/licenses/mit-license.php).
"""

st = input('Bitte geben sie eine Zeichenkette ein >>> ').lower()
voc = input('Bitte geb sie einen Vocal an >>> ').lower()
vocpre = ['a', 'e', 'i', 'o', 'u']

for i in st:
    if i  in vocpre:
        st = st.replace(i, voc)

print(st)
