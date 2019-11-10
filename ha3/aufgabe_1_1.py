def find_pos(string: str, letter: chr):
    return string.index(letter)  # FIXME?


def convert(in_file: str, out_file: str):
    # The file de_DE_frami.dic has the wrong encoding. Without the additional parameter
    # Python will spit out and error.
    
    with open(in_file, 'r', encoding='latin') as read:
        with open(out_file, 'w') as write:
            for line in read.readlines():
                if '#' in line:
                    line = line[:find_pos(line, '#')]
                
                if '/' in line:
                    line = line[:find_pos(line, '/')] + '\n'
                
                line = line.strip()
                write.write(line)
                    
                    
convert('de_DE_frami.dic', 'dictionary.txt')
