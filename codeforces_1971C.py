for _ in range(int(input())):
    a, b, c, d = map(int, input().split())

    a, b = (a, b) if a < b else (b, a)
    count = 0
    if a < c < b:
        count += 1
    if a < d < b:
        count += 1

    if count % 2 == 0:
        print('NO')
    else:
        print('YES')
