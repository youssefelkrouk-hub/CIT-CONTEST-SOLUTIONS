n = int(input())
arr = list(map(int, input().split()))

result = [x for x in arr if x >= 0]

print(len(result))
print(*result)