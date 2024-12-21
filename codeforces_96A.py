from itertools import groupby

inp = input()
lengths = (len(list(x[1])) for x in groupby(inp))

if any(l >= 7 for l in lengths):
    print("YES")
else:
    print("NO")
