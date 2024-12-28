for _ in range(int(input())):
    nstr = input()
    n = int(nstr)
    m = n % 9
    if m == 0:
        print("YES")
        continue

    xs = 0
    ys = 0
    for c in nstr:
        if c == '2':
            xs += 1
        elif c == '3':
            ys += 1

        if xs >= 9 and ys >= 9:
            break

    # 2*x + 6*y + m = 0 (mod 9)
    # 2*x + 6*y = 8*m (mod 9)
    # x + 3*y = 4*m (mod 9)
    # x = 4*m + 6*y (mod 9)

    for y in range(min(ys+1, 9)):
        reqx = (4*m + 6*y) % 9
        if xs >= reqx:
            print("YES")
            break
    else:
        print("NO")
