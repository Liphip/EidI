def count(n: int, i: int = 1) -> int:
    if n <= 1:
            return 1
    elif n == 2:
        return 2
    else:
        return count(n - 1) * count(n - (n - 1) - 1)


array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for i in array:
    print(count(i))
