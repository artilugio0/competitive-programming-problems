def solution1():
    a, b = map(int, input().split())

    x = 3*a - 2*b - 1
    y = b + 1

    if x > b:
        y += x - b + 1
        x = b - 1

    assert(sum([x, b, y])/3 == a)
    assert(x <= b)
    assert(y >= b)

    print(3)
    print(x, b, y)

def editorial_solution():
    a, b = map(int, input().split())

    print(3)
    print(b, b, 3*a - 2*b)

solution1()
