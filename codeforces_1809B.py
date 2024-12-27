def ok(n, cost):
    if cost < 0:
        return False

    return n <= (cost+1)**2

for _ in range(int(input())):
    n = int(input())

    lo = -1
    hi = n
    while lo + 1 < hi:
        mid = (lo+hi)//2
        if not ok(n, mid):
            lo = mid
        else:
            hi = mid

    print(hi)
