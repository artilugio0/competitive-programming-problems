import math

qubes = set(i*i*i for i in range(1, 10000))

for _ in range(int(input())):
    x = int(input())
    top = int(x**(1/3)) + 1

    for a in range(1, top):
        if (x - a*a*a) in qubes:
            print("YES")
            break
    else:
        print("NO")
