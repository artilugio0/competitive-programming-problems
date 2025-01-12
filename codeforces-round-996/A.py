for _ in range(int(input())):
    n, a, b = map(int, input().split())

    d = abs(a - b) +1
    if d % 2 == 1:
        print('YES')
    else:
        print('NO')
