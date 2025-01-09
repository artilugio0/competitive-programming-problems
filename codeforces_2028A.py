for _ in range(int(input())):
    n, a, b = map(int, input().split())
    s = input()

    x, y = 0, 0
    done = False
    for _ in range(20):
        for m in s:
            if m == 'N':
                y += 1
            elif m == 'E':
                x += 1
            elif m == 'S':
                y -= 1
            elif m == 'W':
                x -= 1

            if x == a and y == b:
                print('YES')
                done = True
                break

        if done:
            break
    else:
        print('NO')
