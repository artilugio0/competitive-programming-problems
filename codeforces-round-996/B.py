for _ in range(int(input())):
    n = int(input())
    aa = [int(a) for a in input().split()]
    bb = [int(a) for a in input().split()]

    need = None
    minover = 10**9
    done = False
    for a, b in zip(aa, bb):
        if b > a:
            if need is not None:
                print('NO')
                done = True
                break
            need = b-a
        else:
            minover = min(minover, a - b)

    if done:
        continue

    if need is None:
        print('YES')
    elif need > minover:
        print('NO')
    else:
        print('YES')
