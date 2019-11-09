import time


def find_pos(word, letter):
    for i in range(len(word)):
        if word[i] == letter:
            return i
    return -1


def copyToTxt(source, target):
    s = open(source, 'r')
    t = open(target, 'w')
    sl = s.readlines()
    for i in range(len(sl)):
        word = sl[i]
        if word[0] != '#' and word[0] != '\n':
            pos = find_pos(word, '/')
            t.write(word[:pos] + '\n')
    s.close()
    t.close()
    print('[INFO] File converted!')


if __name__ == '__main__':
    copyToTxt('de_DE_frami.dic', 'dictionary.txt')