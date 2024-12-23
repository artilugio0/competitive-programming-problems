def solve_binary_search():
    for _ in range(int(input())):
        l, r = map(int, input().split())

        # ex:
        # l  l+1  l+1+2  l+1+2+3  l+1+2+3+4
        # 1  2    3      4        5
        # a_n = l + (i-1)*i/2 <= r

        if l == r:
            print(1)
            continue

        a = 1
        b = r+1
        while a < b:
            mid = (a+b)//2
            if l + (mid-1)*mid/2 <= r:
                a = mid + 1
            else:
                b = mid

        a -= 1
        print(a)

solve_binary_search()
