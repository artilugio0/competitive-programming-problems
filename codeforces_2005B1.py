import math
for _ in range(int(input())):
    n, m, q = map(int, input().split())
    aa = [int(a) for a in input().split()]
    d = int(input())

    teacherLeft = -1
    teacherRight = n+1

    for a in aa:
        if a <= d and a > teacherLeft:
                teacherLeft = a
        if a >= d and a < teacherRight:
                teacherRight = a

    if teacherLeft == -1:
        print(teacherRight-1)
        continue
    if teacherRight == n+1:
        print(n - teacherLeft)
        continue

    tld, trd = abs(teacherLeft-d), abs(teacherRight-d)
    x, y = min(tld, trd), max(tld, trd)
    result = x-1 + math.ceil((y-x+1)/2)
    print(result)

