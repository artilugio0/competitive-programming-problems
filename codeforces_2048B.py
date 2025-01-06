import math

for _ in range(int(input())):
    n, k = map(int,input().split())

    sc = math.ceil(n/k)
    m = 1
    t = n
    for i in range(1, n+1):
        if i % k == 0:
            print(m, end=' ')
            m += 1
        else:
            print(t, end=' ')
            t -= 1
    print('')
