for _ in range(int(input())):
    n, m, k = map(int, input().split())

    i = n
    while i > m:
        print(i, end=' ')
        i -= 1

    i = 1
    while i <= m:
        print(i, end=' ')
        i += 1

    print('')

