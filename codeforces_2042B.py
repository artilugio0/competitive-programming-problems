from collections import Counter
import math

for _ in range(int(input())):
    n = int(input())
    ci = Counter(int(c) for c in input().split())

    single = 0
    double = 0

    for m, c in ci.items():
        if c == 1:
            double += 1
        else:
            single += 1

    score = math.ceil(double/2)*2 + single
    print(score)
