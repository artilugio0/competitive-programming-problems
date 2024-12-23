def solve_division():
    t = int(input())
    for _ in range(t):
        legs = int(input())
        cows = legs // 4
        chickens = (legs % 4) // 2

        print(cows + chickens)

def solve_binary_search():
    t = int(input())
    for _ in range(t):
        legs = int(input())
        a = 1
        b = legs

        while a < b:
            mid = (a + b)//2
            if mid*4 < legs:
                a = mid + 1
            else:
                b = mid

        if a*4 == legs:
            result = a
        else:
            result = a-1 + (legs - (a-1)*4)// 2

        print(result)


#solve_division()
solve_binary_search()
