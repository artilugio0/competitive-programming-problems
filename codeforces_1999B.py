for _ in range(int(input())):
    a, b, c, d = map(int, input().split())

    wins = 0
    # a, b  vs c, d
    if a > c and b >= d or a >= c and b > d:
        wins += 1

    # a, b  vs d, c
    if a > d and b >= c or a >= d and b > c:
        wins += 1

    wins *= 2
    print(wins)
