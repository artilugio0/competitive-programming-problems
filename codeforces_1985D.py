for _ in range(int(input())):
    n, m = map(int, input().split())
    rr = [input() for _ in range(n)]

    centercol = None
    centerrow = None

    row = 0
    while row < n:
        col = 0
        while col < m:
            if rr[row][col] == '#' and centercol is None:
                centercol = col
                centerrow = row
                break
            col += 1
        else:
            row += 1
            continue

        break

    lastcol = 10**9
    while row < n:
        col = 0
        while col < m:
            if rr[row][col] == '#':
                if col < lastcol:
                    centerrow = row
                    lastcol = col
            col += 1
        row += 1

    print(centerrow+1, centercol+1)
