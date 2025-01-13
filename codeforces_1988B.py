for _ in range(int(input())):
    n = int(input())
    aa = input()

    c0 = 0
    c1 = 0
    last = None

    for a in aa:
        if a == '1':
            c1 += 1
        elif a == '0' and a != last:
            c0 += 1
        last = a

    if c0 >= c1:
        print('NO')
    else:
        print('YES')
