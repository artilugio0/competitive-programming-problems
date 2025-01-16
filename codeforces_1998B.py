for _ in range(int(input())):
    n = int(input())
    pp = [int(x) for x in input().split()]

    result = pp[1:]
    result.append(pp[0])
    print(' '.join(str(x) for x in result))
