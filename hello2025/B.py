from collections import defaultdict

for _ in range(int(input())):
    n, k = map(int, input().split())
    ai = [int(a) for a in input().split()]

    counts = defaultdict(int)
    for a in ai:
        counts[a] += 1

    oc = list(counts.values())
    oc.sort()

    removed = 0
    for c in oc:
        if k < c:
            break

        if c <= k:
            removed += 1
            k -= c

    print(max(len(oc) - removed, 1))
