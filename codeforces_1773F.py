n = int(input())
a = int(input())
b = int(input())

x, y = min(a,b), max(a,b)

ties = 0
r = []
while x > 0 and n > 1:
    r.append((1, 0))
    x -= 1
    n -= 1

while n > 1:
    if y > 0:
        r.append((0, 1))
        y -= 1
    else:
        r.append((0, 0))
        ties += 1
    n -= 1

r.append((x, y))
if x == y:
    ties += 1

print(ties)
if a < b:
    print('\n'.join(f'{i}:{j}' for i, j in r))
else:
    print('\n'.join(f'{j}:{i}' for i, j in r))
