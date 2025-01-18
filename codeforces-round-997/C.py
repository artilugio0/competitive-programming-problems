for _ in range(int(input())):
    n = int(input())
    aa = [1]
    for i in range(1, n//2+1):
        aa.append(i)

    x = 1
    while len(aa) < n:
        aa.append(x)
        x += 1

    print(' '.join(str(a) for a in aa))
