for _ in range(int(input())):
    p1, p2, p3 = map(int, input().split())
    if p1 % 2 != 0 or p2 % 2 != 0 or p3 % 2 !=0:
        if (p3 - p1 + p2) % 2 != 0 or p3 - p1 + p2 < 0:
            print(-1)
            continue

    p1, p2, p3 = sorted([p1, p2, p3])
    count = 0
    while p1 + p2 > p3:
        count += 1
        p1 -= 1
        p2 -= 1

    count += p1+p2
    print(count)
