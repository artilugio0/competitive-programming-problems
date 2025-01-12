for _ in range(int(input())):
    n = int(input())
    aa = [int(a) for a in input().split()]
    bb = [int(a) for a in input().split()]

    i = 0
    d = 0
    for a, b in zip(aa, bb[1:]):
        d += max(a-b, 0)

    d += aa[-1]
    print(d)
