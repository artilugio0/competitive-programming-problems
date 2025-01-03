n, k = map(int, input().split())
ai = [int(a) for a in input().split()]
bi = [int(b) for b in input().split()]
full = sum(a//b for a, b in zip(ai, bi))

if full < k:
    print(' '.join('0' for _ in range(n)))
    exit(0)

ci = []
for a, b in zip(ai,bi):
    c = a//b
    missing = k - (full - c)
    newc = max(0, missing)
    full = full - c + newc

    ci.append(newc)

print(' '.join(str(c) for c in ci))
