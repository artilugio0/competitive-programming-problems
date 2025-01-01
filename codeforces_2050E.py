# these where the best solutions I could came up with in python.
# the recursive solution breaks because of the large stack
# the second one breaks because of a time limit
# according to the editorial, these solutions are correct, however
# it seems that python is not a good choise for this problem
import sys
sys.setrecursionlimit(100000000)

for _ in range(int(input())):
    s1 = input()
    s2 = input()
    s3 = input()

    cache = {}
    def solve(i, j):
        if (i, j) in cache:
            return cache[(i, j)]

        if i+j == len(s3):
            cache[(i,j)] = 0
            return 0

        a1 = None
        a2 = None

        if i < len(s1):
            a1 = solve(i+1, j) + (1 if s1[i] != s3[i+j] else 0)

        if j < len(s2):
            a2 = solve(i, j+1) + (1 if s2[j] != s3[i+j] else 0)

        a = a1
        if a is None or a2 is not None and a2 < a1:
            a = a2
        cache[(i, j)] = a

        return a

    print(solve(0, 0))

    """
    dp = {
        (len(s1), len(s2)): 0,
    }

    i = len(s1)+1
    while i >= 0:
        i -= 1

        j = len(s2)+1
        while j >= 0:
            j -= 1
            if i == len(s1) and j == len(s2):
                continue

            a1 = float('inf')
            a2 = float('inf')

            if i < len(s1):
                a1 = dp[(i+1, j)] + (0 if s1[i] == s3[i+j] else 1)
            if j < len(s2):
                a2 = dp[(i, j+1)] + (0 if s2[j] == s3[i+j] else 1)

            dp[(i, j)] = min(a1, a2)


    print(dp[(0,0)])
    """
