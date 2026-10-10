n, k = map(int, input().split())
arr = list(map(int, input().split()))

 # my idea is to use a helper function to count the negative number then use a selection window to check if there is a sublist that count of negative <=K

def count_neg(L):
    t=0
    for i in range(len(L)):
        if L[i]<0:
            t=t+1
    return t
best=0
for i in range(len(arr)):
    for j in range(i,len(arr)):
        window = arr[i:j+1]
        if count_neg(window) <= k:
            best=max(best,len(window))
print(best)
            