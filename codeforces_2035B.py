for _ in range(int(input())):
    n = int(input())

    if n%2 == 0:
        print('3'*(n-2) + '66')
    elif n <= 3:
        print(-1)
    else:
        print('3'*(n-4) + '6366')
