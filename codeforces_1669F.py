for _ in range(int(input())):
    n = int(input())
    wi = [int(w) for w in input().split()]

    best = 0

    s = 0
    sp = 0
    e = 0
    ep = -1

    for i in range(len(wi)):
        if s <= e:
            s += wi[sp]
            sp += 1
        else:
            e += wi[ep]
            ep -= 1

        if s == e:
            best = i+1

    print(best)
