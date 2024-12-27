for _ in range(int(input())):
    n, x = map(int, input().split())
    ai = [int(a) for a in input().split()]

    ai.sort()

    def ok(h):
        s = 0
        for a in ai:
            if a < h:
                s += h - a
        return s <= x

    lo = 0
    hi = 10**10
    while lo + 1 < hi:
        mid = (lo+hi)//2
        if ok(mid):
            lo = mid
        else:
            hi = mid
    print(lo)
