import math

for _ in range(int(input())):
    w, b = map(int, input().split())

    # (n*(n+1))//2 == w + b
    # (n*(n+1)) == 2*w + 2*b
    # n**2 + n - 2*w - 2*b == 0
    # n = (-1 + math.sqrt(1 -8(w+b))) / 2

    n = int((-1 + math.sqrt(1 +8*(w+b))) / 2)
    print(n)
