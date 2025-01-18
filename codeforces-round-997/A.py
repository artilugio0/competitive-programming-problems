for _ in range(int(input())):
    n, m = map(int, input().split())

    p = m*4

    input()
    for _ in range(n-1):
        x, y = map(int, input().split())
        p += 2*x + 2*y

    print(p)

