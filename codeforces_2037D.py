import heapq

for _ in range(int(input())):
    n, m, L = map(int, input().split())
    hi = [tuple(map(int, input().split())) for _ in range(n)]
    pi = [tuple(map(int, input().split())) for _ in range(m)]

    i = 0
    pups = [] # heap using negated values to use it as a max heap
    v = 1
    count = 0
    for hl, hr in hi:
        while i < len(pi) and pi[i][0] < hl:
            heapq.heappush(pups, -pi[i][1])
            i += 1
        need = hr - hl + 2
        while pups and v < need:
            count += 1
            v += -heapq.heappop(pups)

        if v < need:
            print(-1)
            break
    else:
        print(count)
