for _ in range(int(input())):
    n = int(input())
    pp = [int(p) for p in input().split()]

    if len(pp) <= 2:
        print('YES')
        continue

    for i in range(len(pp)-1):
        if pp[i] == i+1:
            continue
        if pp[i+1] == i+1 and pp[i] == i+2:
            pp[i], pp[i+1] = pp[i+1], pp[i]
            continue

        print('NO')
        break
    else:
        print('YES')

