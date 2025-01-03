for _ in range(int(input())):
    n = int(input())
    ai = [int(a) for a in input().split()]

    for i in range(len(ai)):
        a = ai[i] 
        a_1 = ai[i-1] if i > 0 else None

        b = ai[-i-1]
        bp1 = ai[-i] if i > 0 else None

        if a == a_1 or b == bp1:
            ai[i], ai[-i-1] = ai[-i-1], ai[i]

    count = 0
    for a1, a2 in zip(ai, ai[1:]):
        if a1 == a2:
            count += 1
    print(count)
