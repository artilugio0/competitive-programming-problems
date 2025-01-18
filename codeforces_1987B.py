import heapq

for _ in range(int(input())):
    n = int(input())
    aa = [int(a) for a in input().split()]

    m = aa[0]
    less = []
    sum = 0
    coins = 0
    for i in range(1, len(aa)):
        if aa[i] < m:
            heapq.heappush(less, m - aa[i])
            continue
        m = max(m, aa[i])

    while less:
        l = heapq.heappop(less)
        coins += (len(less)+1+1)*(l-sum)
        sum = l

    print(coins)
