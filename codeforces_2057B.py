from collections import defaultdict, Counter

def failed_solution():
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

def solution():
    # will be used for xoring the keys of the dict to avoid hash collisions
    #   which broke the previous solution
    from random import getrandbits
    rnd = getrandbits(32)


    for _ in range(int(input())):
        n, k = map(int, input().split())
        ai = [int(a)^rnd for a in input().split()]

        counts = defaultdict(int)
        for a in ai:
            counts[a] += 1

        oc = list(counts.values())
        oc.sort()

        removed = 0
        for c in oc:
            if k < c:
                break

            removed += 1
            k -= c

        print(max(len(oc) - removed, 1))


solution()
