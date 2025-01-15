for _ in range(int(input())):
    n = int(input())
    s = input()

    ucount = sum(1 for c in s if c == 'U')
    if ucount % 2 == 0:
        print('NO')
    else:
        print('YES')
