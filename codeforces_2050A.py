for _ in range(int(input())):
    n, m = map(int, input().split())
    count = 0
    used = 0
    done = False

    for _ in range(n):
        s = input()
        if done:
            continue

        if len(s) + used > m:
            done = True
            continue

        count += 1
        used += len(s)

    print(count)
