n, t = map(int, input().split())
arr = list(map(int, input().split()))
# write your code here 
pos = {}  # value -> list of indices (1-based) in increasing order
for idx, v in enumerate(arr, 1):
    pos.setdefault(v, []).append(idx)

best = None
for i, v in enumerate(arr, 1):
    need = t - v
    if need in pos:
        for j in pos[need]:
            if j > i:
                best = (i, j)
                break
    if best:
        break

if best:
    print(best[0], best[1])
else:
    print(-1, -1)