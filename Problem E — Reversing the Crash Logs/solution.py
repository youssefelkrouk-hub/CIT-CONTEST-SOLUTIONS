
N = int(input())
strings = input().split()
# write your code here

import sys

# si les logs sont donnes un par ligne, on lit le reste
while len(strings) < N:
    line = sys.stdin.readline()
    if not line: 
        break
    strings += line.split()

target = "citlogin"[::-1]

count = 0
for s in strings[:N]:
    if target in s:
        count += 1

print(count)
