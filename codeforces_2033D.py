for _ in range(int(input())):
    n = int(input())
    ai = [int(a) for a in input().split()]

    s = 0
    count = 0

    seen = set([0])
    for a in ai:
        s += a
        if s in seen:
            count += 1
            seen = set([0])
            s = 0
        else:
            seen.add(s)

    print(count)
