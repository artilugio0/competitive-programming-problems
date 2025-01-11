for _ in range(int(input())):
    n = int(input())
    aa = [int(a) for a in input().split()]

    for a1, a2 in zip(aa, aa[1:]):
        if 2*a1 > a2 and 2*a2 > a1:
            print('YES')
            break
    else:
        print('NO')
