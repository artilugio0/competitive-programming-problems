for _ in range(int(input())):
    n, m, k = map(int, input().split())

    need = (n // m)*(m-1) + max((n%m) - 1, 0)
    if k >= need:
        print('NO')
    else:
        print('YES')
