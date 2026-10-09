n, t = map(int, input().split())
arr = list(map(int, input().split()))

pos = {}  # valeur -> liste des indices (1-based) en ordre croissant
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