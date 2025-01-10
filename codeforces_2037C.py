for _ in range(int(input())):
    n = int(input())

    if n <= 4:
        print(-1)
        continue

    result = []
    p = n if n % 2 == 1 else n-1
    while p > 5:
        result.append(p)
        p -= 2

    result.extend([1,3,5,4,2])

    p = 6
    while p <= n:
        result.append(p)
        p += 2

    print(' '.join(str(r) for r in result))
