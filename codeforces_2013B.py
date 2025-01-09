for _ in range(int(input())):
    n = int(input())
    aa = [int(a) for a in input().split()]
    result = sum(aa) - 2*aa[-2]
    print(result)
