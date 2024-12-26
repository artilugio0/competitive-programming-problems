def ok(ai, c):
    if c == 0:
        return True

    if c > len(ai)//2 - (len(ai)+1)%2:
        return False

    for i in range(c):
        if ai[i] >= ai[i-1-c] or ai[i] >= ai[i-c]:
            return False
    return True


n = int(input())
ai = [int(x) for x in input().split()]

ai.sort()

lo = 0
hi = len(ai)
while lo + 1 < hi:
    mid = (lo+hi)//2
    if ok(ai, mid):
        lo = mid
    else:
        hi = mid

best = lo

result = []
for a, b in zip(ai[:best], ai[-(best+1):]):
    result.append(b)
    result.append(a)

result.append(ai[-1])

for a in ai[best:-(best+1)]:
    result.append(a)

print(best)
print(' '.join(str(a) for a in result))
