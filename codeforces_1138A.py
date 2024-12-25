input()
ti = [int(t) for t in input().split()]

tuna = 0
eel = 0
best = 0
last = None
for t in ti:
    if t == 1:
        if last != t:
            tuna = 0
        tuna += 1

        if tuna <= eel and tuna > best:
            best = tuna

    elif t == 2:
        if last != t:
            eel = 0
        eel += 1

        if eel <= tuna and eel > best:
            best = eel
    else:
        raise(f"unexpected value {t}")

    last = t

print(best*2)

