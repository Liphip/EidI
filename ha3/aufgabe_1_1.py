def find_pos(string: str, letter: chr):
    return string.index(letter)


def convert(in_file: str, out_file: str):
    # de_DE_frami.dic ist falsch encodiert (auf jeden fall für mich, nutze Arch Linux) und muss
    # deshalb mit dem encoding 'latin' eingelesen werden, um Fehler zu verhindern.

    with open(in_file, 'r', encoding='latin') as read:
        with open(out_file, 'w', encoding='utf-8') as write:
            for line in read.readlines():
                if '#' in line:
                    line = line[:find_pos(line, '#')]

                if '/' in line:
                    line = line[:find_pos(line, '/')]

                line = line.strip()

                if len(line) != 0:
                    write.write(line + '\n')


convert('de_DE_frami.dic', 'dictionary.txt')
