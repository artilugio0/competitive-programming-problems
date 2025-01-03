# this solution is incorrect

for _ in range(int(input())):
    n = int(input())
    ai = [int(a) for a in input().split()]

    ai.sort()

    best = 10**9
    p1 = -1
    p2 = 0
    while p2 < len(ai):
        while p2+1 < len(ai) and ai[p2+1] == ai[p2]:
            p2 += 1

        minum = ai[p2]//2+1

        while p1+1 < p2 and ai[p1+1] < minum:
            p1 += 1

        change = (len(ai) - (p2 + 1))
        change += p1 + 1

        best = min(best, change)

        p2 += 1

    print(best)
