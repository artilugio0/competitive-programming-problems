"""
5
5                       101
2 1 3 4 5 

0
0
1
1
101





6
7                       111
1 2 4 6 5 3 

7
7                       111
2 4 5 1 3 6 7 

8
15                      1111
2 4 5 1 3 6 7 8 

9
9                       1001
2 4 5 6 7 1 3 8 9 

10
15                      1111
1 2 3 4 5 6 8 10 9 7 

if odd  --> target: if n <= 3       n - 1
if odd  --> target: else:           n
if even --> target: if n <= 4:      n
                    else:           int(math.log2(n)+1)**2 -1


ODD:
3   = 0000011
1   = 0000001
n-1 = 1XXXXX0
n   = 1XXXXX1

...
...
| 3
& 1
| (n-1)
& n


EVEN:

a      = 0111110
1      = 0000001
b      = 0YXXYY1
n      = 1XYYXX0
target = 1111111


a      = 0111111
n-1    = 0111111
n      = 1000000
target = 1111111

"""

# TODO: this answer is incorrect. Revisit this problem later

import math

cache = {}
def solve(n):
    if n in cache:
        return cache[n]

    if n % 2 == 1:
        ans = [i for i in range(2,n-1) if i != 3]
        ans.append(3)
        ans.append(1)
        ans.append(n-1)
        ans.append(n)
        cache[n] = (n, ans)
        return n, ans
    elif n == 6:
        cache[n] = (7, [1, 2, 4, 6, 5, 3])
        return 7, [1, 2, 4, 6, 5, 3]

    if math.log2(n) == int(math.log2(n)):
        _, ans = solve(n-2)
        ans.append(n-1)
        ans.append(n)
    else:
        a = (1<<int(math.log2(n)))-1
        b = n^a
        ans = [i for i in range(1,n) if i != a and i != b]
        ans.append(a)
        ans.append(b)
        ans.append(n)

    return 1<<(int(math.log2(n)+1)-1), ans


for _ in range(int(input())):
    n = int(input())

    a, ans = solve(n)

    print(a)
    print(' '.join(str(x) for x in ans))

    r = 0
    for (i, x) in enumerate(ans, start=1):
        if i % 2 == 1:
            r = r & x
        else:
            r = r | x
    assert(r==a)
