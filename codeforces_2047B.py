from collections import Counter

for _ in range(int(input())):
    n = int(input())
    s = input()

    ss = Counter(s)

    bestmax = 0
    bestmin = n+1
    maxc = None
    minc = None

    for c, count in ss.items():
        if count > bestmax:
            bestmax = count
            maxc = c
        if count <= bestmin:
            bestmin = count
            minc = c

    done = False
    for c in s:
        if not done and c == minc and maxc is not None:
            print(maxc, end='')
            done = True
        else:
            print(c, end='')

    print('')
