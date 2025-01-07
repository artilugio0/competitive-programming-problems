for _ in range(int(input())):
    s = input()
    if len(s) == 1:
        print(-1)
        continue
    elif len(s) >= 2 and s[0] == s[1]:
        print(s[:2])
        continue
    elif len(s) == 2 and s[0] != s[1]:
        print(-1)
        continue

    l = 0
    while l+2 < len(s):
        if s[l+1] == s[l+2]:
            print(s[l+1:l+3])
            break
        if s[l] != s[l+1] and s[l] != s[l+2] and s[l+1] != s[l+2]:
            print(s[l:l+3])
            break
        l += 1
    else:
        print(-1)

