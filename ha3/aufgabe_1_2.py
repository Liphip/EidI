word = input('> ')

with open('dictionary.txt', 'r') as read:
    lines = read.readlines()
    
    for i in range(len(lines)):
        if lines[i].replace('\n', '') == word:
            print(i + 1)
            break
