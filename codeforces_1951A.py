for _ in range(int(input())):
    n = int(input())
    s = input()

    adj = False
    ones = 0
    for a, b in zip(s, s[1:]):
        if a == '1':
            ones += 1
            if b == '1':
                adj = True

    if s[-1] == '1':
        ones += 1

    if ones % 2 == 1:
        print('NO')
    elif ones == 2 and adj:
        print('NO')
    else:
        print('YES')


