for _ in range(int(input())):
    n, x, y = map(int, input().strip().split())

    result = [None]*n
    for i in range(0, n):
        fs = set([result[(i-1)%n], result[(i+1)%n]])

        if i == x-1:
            fs.add(result[(y-1)%n])
        elif i == y-1:
            fs.add(result[(x-1)%n])

        if 0 not in fs:
            result[i] = 0
        elif 1 not in fs:
            result[i] = 1
        else:
            result[i] = 2

    print(' '.join(str(r) for r in result))
