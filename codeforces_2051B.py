for _ in range(int(input())):
    n, a, b, c = map(int, input().split())
    s = a + b + c

    d3 = n//s

    if d3 != 0 and n % s == 0:
        print(d3*3)
    elif d3*s + a >= n:
        print(d3*3+1)
    elif d3*s + a + b >= n:
        print(d3*3+2)
    elif d3*s + a + b + c >= n:
        print(d3*3+3)
    else:
        raise Exception("invalid case")
