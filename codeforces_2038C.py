from collections import defaultdict

for _ in range(int(input())):
    n = int(input())
    ai = [int(a) for a in input().split()]
    ai.sort()

    counts = defaultdict(int)
    for a in ai:
        counts[a] += 1

    x1, y1, x2, y2 = None, None, None, None
    for a in ai:
        if counts[a] < 2:
            continue

        if x1 is None:
            x1 = a
            counts[a] -= 2
            if counts[a] >= 2:
                y1 = a
                counts[a] -= 2
        elif y1 is None:
            y1 = a
            counts[a] -= 2
        else:
            break

    if x1 is None or y1 is None:
        print('NO')
        continue

    for i in range(len(ai)):
        a = ai[-i-1]

        if counts[a] < 2:
            continue

        if x2 is None:
            x2 = a
            counts[a] -= 2
            if counts[a] >= 2:
                y2 = a
                counts[a] -= 2
        elif y2 is None:
            y2 = a
            counts[a] -= 2
        else:
            break

    if x2 is None or y2 is None:
        print('NO')
        continue

    if abs(x1-x2)*abs(y1-y2) < abs(x1-y2)*abs(y1-x2):
        x2, y2 = y2, x2

    print('YES')
    print(x1,y1,x2,y1,x1,y2,x2,y2)
