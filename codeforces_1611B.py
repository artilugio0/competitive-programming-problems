for _ in range(int(input())):
    a, b = map(int, input().split())
    if b < a:
        a, b = b, a

    l = 0
    h = a+b
    while l < h:
        mid = (l+h)//2
        if mid*4 <= a+b and mid <= a:
            l = mid + 1
        else:
            h = mid

    l = l - 1
    print(max(l, 0))
