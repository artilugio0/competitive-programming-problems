for _ in range(int(input())):
    n = int(input())
    ai = [int(a) for a in input().strip().split()]

    s0 = 0
    s1 = 0
    for i, d in enumerate(ai):
        if i % 2 == 0:
            s0 += d
        else:
            s1 += d

    s0c = len(ai)//2 + len(ai) % 2
    s1c = len(ai)//2

    if s0 % s0c == 0 and s1 % s1c == 0 and s0//s0c == s1//s1c:
        print("YES")
    else:
        print("NO")

