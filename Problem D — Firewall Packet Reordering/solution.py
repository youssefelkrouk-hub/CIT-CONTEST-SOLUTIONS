m, k = map(int, input().split())
arr = list(map(int, input().split()))
#write your code here
left = 0
neg = 0
best = 0

for right in range(m):
    if arr[right] < 0:
        neg += 1
    while neg > k:
        if arr[left] < 0:
            neg -= 1
        left += 1
    best = max(best, right - left + 1)

print(best)