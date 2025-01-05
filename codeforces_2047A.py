import math

for _ in range(int(input())):
    n = int(input())
    ai = [int(a) for a in input().split()]

    count = 0
    total = 0
    for a in ai:
        total += a
        s = math.sqrt(total)
        if s == int(s) and s %2 == 1:
            count += 1

    print(count)

