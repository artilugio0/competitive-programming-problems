from collections import defaultdict

for _ in range(int(input())):
    n, k = map(int, input().split())
    aa = [int(a) for a in input().split()]

    rems = defaultdict(list)
    for i, a in enumerate(aa):
        rems[a%k].append(i)

    for r, l in rems.items():
        if len(l) == 1:
            print('YES')
            print(l[0]+1)
            break
    else:
        print('NO')
