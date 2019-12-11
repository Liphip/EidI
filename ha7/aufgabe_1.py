def next_palindrome(num,k):
    while k > 0:
        palindrome = True
        for i in range(len(num) // 2):
            if num[i] != num[-1 -i]:
                palindrome = False
                break
            
        if palindrome:
            k -= 1
            print('palindrome:' + num)
            num = str(int(num) + 1)
        else:
            num = str(int(num) + 1) 

# Die Funktion addiere ist hier nur der Vollständigkeit halber aufgeführt.
def addiere(n,m):
    while n > 0:
        if m > 100:
            print(m)
            break
        else:
            m = m + n
            n = n-1

if __name__ == "__main__":
    # F\"uhren Sie hier den Glass Box Test fuer Funktion next_palindrome durch

    next_palindrome("23",3) ## for nur für 0
    next_palindrome('123',0) ## nicht in while schleife
    next_palindrome('22',1) ## in true zweig von zweitem if
    next_palindrome('23',1) ## in erstes if und in else von letztem if
