for _ in range(int(input())):
    n = int(input())
    ai = [int(a) for a in input().split()]

    counts = {}
    maxc = 0
    for a in ai:
        counts[a] = counts.get(a, 0) + 1
        maxc = max(maxc, counts[a])

    def ok(x):
        if x == len(counts):
            return maxc-1 >= x

        return len(counts) >= x and maxc >= x

    lo = 0
    hi = n + 1
    while lo + 1 < hi:
        mid = (lo+hi)//2
        if ok(mid):
            lo = mid
        else:
            hi = mid

    print(lo)
