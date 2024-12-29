from collections import defaultdict, deque

# NOTE:this solution does not work
# it reaches the time limit for some test cases
# TODO: make it more efficient

def solve(g, s):
    best = 0
    next = [s]
    seen = set()
    while next:
        a = next.pop()
        if a in seen:
            continue
        seen.add(a)

        best = max(best, a)

        for n in g[a]:
            if n != a:
                next.append(n)

    return best


for _ in range(int(input())):
    n = int(input())
    ai = (int(a) for a in input().split())

    g = defaultdict(set)
    for i, a in enumerate(ai):
        req = a + i
        g[req].add(req + i)

    print(solve(g, n))
