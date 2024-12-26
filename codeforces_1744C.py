for _ in range(int(input())):
    _, x = input().split()
    s = input()

    fg = None
    started = False
    best = 0
    count = 0
    for i, c in enumerate(s):
        if c == x:
            started = True

        if c == 'g':
            if started and count > best:
                best = count

            if fg is None:
                fg = i

            count = 0
            started = False
        elif started:
            count += 1

    if started and count + fg > best:
        best = count + fg

    print(best)
