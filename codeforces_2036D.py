def next_cell(l, n, m, r, c):
    if r == l and c < m - l -1:
        return (r, c+1)
    elif r < n - l - 1 and c == m - l -1: 
        return (r+1, c)
    elif r == n - l - 1 and c > l:
        return (r, c-1)
    elif r == n - l - 1 and c > l:
        return (r, c-1)
    elif r > l and c == l:
        return (r-1, c)


for _ in range(int(input())):
    n, m = map(int, input().split())
    ci = [[int(c) for c in input()] for _ in range(n)]

    layers = min(n//2, m//2)
    count = 0
    for l in range(layers):
        row, col = l, l
        for i in range(2*((n-2*l)+(m-2*l)-2)):
            c1 = ci[row][col]

            nr, nc = next_cell(l, n, m, row, col)
            c2 = ci[nr][nc]

            nr, nc = next_cell(l, n, m, nr, nc)
            c3 = ci[nr][nc]

            nr, nc = next_cell(l, n, m, nr, nc)
            c4 = ci[nr][nc]

            if c1 == 1 and c2 == 5 and c3 == 4 and c4 == 3:
                count += 1

            row, col = next_cell(l, n, m, row, col) 

    print(count)
