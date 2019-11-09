def posInDoc(document, word):
    doc = open(document, 'r')
    doclist = doc.readlines()
    length = len(doclist)
    for i in range(length):
        if doclist[i] == word + '\n':
            return i
    

if __name__ == '__main__':
    word = input('Bitte geben sie das Wort an, dessen Position sie feststellen wollen >>>')
    print('Das Wort ' + word + ' wird zum ersten Mal in Zeile ' + str(
        posInDoc('dictionary.txt', word)) + ' in dieser Schreibweise genannt.')
