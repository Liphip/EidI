"""
Copyright (c) 2019  Luis Michaelis, Philip Laskowicz
Licensed under MIT (https://opensource.org/licenses/mit-license.php).
"""

word = input('Geben sie das Wort ein, das sie suchen > ')

with open('dictionary.txt', 'r', encoding='utf-8') as read:
    lines = read.readlines()

    for i in range(len(lines)):
        if lines[i].replace('\n', '') == word:
            print(i + 1)
            break
