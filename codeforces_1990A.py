for _ in range(int(input())):
    n = int(input())
    aa = [int(a) for a in input().split()]

    aa.sort(key=lambda a: -a)

    i = 0

    while i < len(aa):
        count = 0
        e = aa[i]
        while i < len(aa) and aa[i] == e:
            i += 1
            count += 1

        if count % 2 == 1:
            print('YES')
            break

    else:
        print('NO')
