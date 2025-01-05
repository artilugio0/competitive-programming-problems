for _ in range(int(input())):
    l, r = map(int, input().split())

    lo = l
    hi = r

    m = 2**(len("{0:b}".format(r)) + 1) -2

    while lo+1 < hi:
        mid = (lo+hi)//2
        h = (l^r) + (l^mid) + (r^mid)
        if r <= m:
            lo = mid
        else:
            hi = mid

    print(l, lo, r)
