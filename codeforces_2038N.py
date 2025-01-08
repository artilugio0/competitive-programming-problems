for _ in range(int(input())):
    s = input()
    if s[0] < s[2]:
        print(f'{s[0]}<{s[2]}')
    elif s[0] == s[2]:
        print(f'{s[0]}={s[2]}')
    elif s[0] > s[2]:
        print(f'{s[0]}>{s[2]}')
