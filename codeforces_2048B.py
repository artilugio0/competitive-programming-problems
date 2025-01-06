import math

def solution1():
    for _ in range(int(input())):
        n, k = map(int,input().split())

        m = 1
        t = n
        for i in range(1, n+1):
            if i % k == 0:
                print(m, end=' ')
                m += 1
            else:
                print(t, end=' ')
                t -= 1
        print('')

def solution2():
    for _ in range(int(input())):
        n, k = map(int,input().split())

        reserved = n//k
        r = 1
        nr = reserved + 1
        for i in range(1, n+1):
            if r <= reserved and (i % k == 0 or nr > n):
                print(r, end=' ')
                r += 1
            else:
                print(nr, end=' ')
                nr += 1
        print('')

solution2()
