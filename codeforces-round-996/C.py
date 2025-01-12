for _ in range(int(input())):
    n, m = map(int, input().split())
    s = input()
    aa = [[int(a) for a in input().split()] for _ in range(n)]

    r, c = 0, 0
    for d in s:
        if d == 'D':
            v = sum(aa[r][i] for i in range(m))
            aa[r][c] = -v
            r += 1
        else:
            v = sum(aa[i][c] for i in range(n))
            aa[r][c] = -v
            c += 1

    v = sum(aa[n-1][i] for i in range(m))
    aa[n-1][m-1] = -v

    for i in range(n):
        print(' '.join(str(a) for a in aa[i]))
