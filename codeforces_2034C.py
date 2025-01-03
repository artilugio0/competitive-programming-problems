"""
This solution hits a TLE on code forces. The same logic implemented in golang passes all tests.
Not sure if there is anything wrong with the code that makes it slow
"""

import sys
sys.setrecursionlimit(1000000000)

def move(r, c, mv):
    if mv == 'U':
        return (r-1, c)
    if mv == 'R':
        return (r, c+1)
    if mv == 'D':
        return (r+1, c)
    if mv == 'L':
        return (r, c-1)

    raise('invalid move')


for _ in range(int(input())):
    n, m = map(int, input().split())
    ri = [[c for c in input()] for _ in range(n)]
    assert(m == len(ri[0]))

    cache = {}
    def bad_cell(r, c, visited):
        stack = [(r,c)]
        if (r,c) in cache:
            return cache[(r,c)]

        if (r,c) in visited:
            cache[(r,c)] = True
            return True

        if r < 0 or c < 0 or r >= n or c >= m:
            cache[(r,c)] = False
            return False

        if ri[r][c] != '?':
            nr, nc = move(r,c,ri[r][c])

            visited.add((r,c))
            result = bad_cell(nr, nc, visited)
            visited.remove((r,c))

            cache[(r,c)] = result
            return result

        for mv in 'URDL':
            nr, nc = move(r,c,mv)

            visited.add((r,c))
            isbad = bad_cell(nr, nc, visited)
            visited.remove((r,c))

            if isbad:
                cache[(r,c)] = True
                return True

        cache[(r,c)] = False
        return False

    count = 0
    for r in range(n):
        for c in range(m):
            if bad_cell(r, c, set()):
                count += 1

    print(count)
