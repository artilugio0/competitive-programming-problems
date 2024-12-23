import heapq
k = list(map(int, input().split()))[1]

q = [int(x) for x in input().split()]
heapq.heapify(q)

antenna_needed_at = q[0] + k
covered = 0
count = 0
prev = 0
while q:
    h = heapq.heappop(q)
    if h > covered and antenna_needed_at is None:
        antenna_needed_at = h + k

    if h == antenna_needed_at:
        count += 1
        covered = h + k
        antenna_needed_at = None
    elif antenna_needed_at is not None and h > antenna_needed_at:
        count += 1
        covered = prev + k
        if covered >= h:
            antenna_needed_at = None
        else:
            antenna_needed_at = h + k

    prev = h

if prev > covered:
    count += 1

print(count)
