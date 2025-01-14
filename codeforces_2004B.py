for _ in range(int(input())):
    a, b = map(int, input().split())
    c, d = map(int, input().split())

    (a,b), (c,d) = sorted([(a, b), (c,d)])

    if b + 1 <= c:
        print(1)
    elif b == c:
        print(2)
    elif a < c < b and b < d:
        print(b - c + 2)
    elif a < c < b and b > d:
        print(d - c + 2)
    elif a < c < b and b == d:
        print(d - c + 1)
    elif a == c and b < d:
        print(b - a + 1)
    elif a == c and b > d:
        print(d - a + 1)
    elif a == c and b == d:
        print(d - a)
