n = int(input())
xi = [int(x) for x in input().split()]

mi = []
for _ in range(int(input())):
    mi.append(int(input()))

xi.sort()
for m in mi:
    lo = 0
    hi = len(xi)+1

    while lo + 1 < hi:
        mid = (lo+hi)//2
        if mid == 0 or mid <= len(xi) and xi[mid-1] <= m:
            lo = mid
        else:
            hi = mid

    print(lo)
