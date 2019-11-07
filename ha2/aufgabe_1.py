"""
Copyright (c) 2019  Luis Michaelis, Philip Laskowicz
Licensed under MIT (https://opensource.org/licenses/mit-license.php).
"""

st = input('Bitte geben sie eine Zeichenkette ein >>> ').lower()
voc = input('Bitte geb sie einen Vocal an >>> ').lower()

for i in ['a', 'e', 'i', 'o', 'u']:
    st = st.replace(i, voc)

print(st)
