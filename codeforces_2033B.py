for _ in range(int(input())):
    n = int(input())
    m = [[int(x) for x in input().split()] for _ in range(n)]

    result = 0
    for i in range(1, n):
        minu = 10**6
        minl = 10**6
        for j in range(0, n-i):
            minu = min(minu, m[j][i+j])
            minl = min(minl, m[i+j][j])

        if minu < 0:
            result += abs(minu)
        if minl < 0:
            result += abs(minl)

    mind = 10**6
    for i in range(0, n):
        mind = min(mind, m[i][i])

    if mind < 0:
        result += abs(mind)

    print(result)

