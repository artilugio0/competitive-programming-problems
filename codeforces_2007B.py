for _ in range(int(input())):
    n, m = map(int, input().split())
    aa = [int(a) for a in input().split()]

    amax = 0
    for a in aa:
        amax = max(a, amax)

    result = []
    for _ in range(m):
        [op, l, r] = input().split()
        l = int(l)
        r = int(r)

        if l <= amax <= r:
            if op == '+':
                amax += 1
            else:
                amax -= 1

        result.append(amax)

    print(' '.join(str(r) for r in result))

