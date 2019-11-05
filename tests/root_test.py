
def root(base = 8, n = 2, eps = 1):
    """
    'n'-th root of 'base' with accuracy of 10^-6*'eps'.
    :param n:
    :param base:
    :param eps:
    :return:
    """
    if -1 < base < 1:
        print("Please enter a number smaller than -1 or greater than 1.")
        return 1
    elif base < 0 and n%2==0:
        print("There is no even root of an negative number.")
        return 1
    eps = eps * (10**-6)
    left = 0
    right = base
    value = (left + right) / 2
    while abs(value ** n - base) >= eps:
        if value ** n < base:
            left = value
        else:
            right = value
        value = (left + right) / 2
    return value

inp = input("Please enter either one, two or three numbers separated by | >>> ").split("|")
if len(inp) == 1:
    base = int(inp[0])
    print(root(base))
elif len(inp) == 2:
    base = int(inp[0])
    n = int(inp[1])
    print(root(base, n))
elif len(inp) == 3:
    base = int(inp[0])
    n = int(inp[1])
    eps = int(inp[2])
    print(root(base, n ,eps))
else:
    print("Please restart and enter one, two or three Numbers separated by '|'.")
    exit(-1)
exit(1)
