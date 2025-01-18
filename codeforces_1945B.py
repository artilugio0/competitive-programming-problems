for _ in range(int(input())):
    a, b, m = map(int, input().split())
    result = m//a + m//b + 2
    print(result)
