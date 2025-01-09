import math

for _ in range(int(input())):
    x, y ,k = map(int, input().split())

    m = min(x, y)
    a, b = m, 0
    while math.sqrt(a*a + b*b) < k:
        b += 1

    print(0,0,a,b)
    print(0,a,b,0)

