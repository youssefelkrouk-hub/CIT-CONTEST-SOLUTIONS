n, k = map(int, input().split())
numbers = list(map(int, input().split()))
# write your code here

low = max(numbers)
high = sum(numbers)

while low < high:
    limit = (low + high) // 2

    groups = 1
    current = 0
    for x in numbers:
        if current + x > limit:
            groups = groups + 1
            current = x
        else:
            current = current + x

    if groups <= k:
        high = limit
    else:
        low = limit + 1

print(low)