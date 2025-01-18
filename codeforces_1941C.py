for _ in range(int(input())):
    n = int(input())
    s = input()

    i = 0
    count = 0
    while i < len(s)-2:
        if (s[i],s[i+1],s[i+2]) == ('m', 'a', 'p'):
            count += 1
            if i+4 < len(s) and s[i+3] == 'i' and s[i+4] == 'e':
                i += 5
                continue
            i += 3
            continue

        elif (s[i],s[i+1],s[i+2]) == ('p', 'i', 'e'):
            count += 1
            i += 3
            continue

        i += 1

    print(count)
