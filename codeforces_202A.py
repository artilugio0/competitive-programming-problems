s = input()

count = 0
maxc = ''
for c in s:
    if c > maxc:
        maxc = c
        count = 1
    elif c == maxc:
        count += 1

print(maxc*count)
