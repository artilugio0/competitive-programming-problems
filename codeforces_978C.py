input()
ai = [int(a) for a in input().split()]
bi = [int(b) for b in input().split()]

s = 0
for i, a in enumerate(ai):
    s += a
    ai[i] = s

cache = {}

for b in bi:
    lo = -1
    hi = len(ai)
    while lo + 1 < hi:
        mid = (lo+hi)//2
        if ai[mid] < b:
            lo = mid
        else:
            hi = mid

    d = hi+1
    if hi > 0:
        r = b - ai[hi-1]
    else:
        r = b

    print(d, r, sep=' ')
