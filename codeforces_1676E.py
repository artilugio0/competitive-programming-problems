for _ in range(int(input())):
    n, q = map(int, input().split())
    ai = [int(a) for a in input().split()]

    ai.sort(key=lambda a: -a)
    s = 0
    si = []
    for a in ai:
        s += a
        si.append(s)

    for _ in range(q):
        x = int(input())

        lo = -1
        hi = len(si)
        while lo + 1 < hi:
            mid = (lo+hi)//2
            if si[mid] < x:
                lo = mid
            else:
                hi = mid
        if hi == len(si):
            print(-1)
        else:
            print(hi+1)
