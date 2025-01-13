for _ in range(int(input())):
    n, k = map(int, input().split())

    count = 0
    while n > 1:
        n -= k-1
        count += 1

    print(count)
