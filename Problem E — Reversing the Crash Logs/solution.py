import sys

data = sys.stdin.read().split()
n = int(data[0])
logs = data[1:1 + n]

target = "citlogin"[::-1]

count = 0
for s in logs:
    if target in s:
        count += 1

print(count)