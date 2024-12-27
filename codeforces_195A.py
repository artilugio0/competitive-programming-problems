a, b, c = map(int, input().split())

def ok(w):
    if w < 0:
        return False

    available = w*b
    t = 0
    while True:
        available += b
        available -= a
        if available < 0:
            return False

        t += 1

        if t == c:
            return True

lo = -1
hi = c*a// b + 1
while lo + 1 < hi:
    mid = (lo+hi)//2
    if not ok(mid):
        lo = mid
    else:
        hi = mid

print(hi)

