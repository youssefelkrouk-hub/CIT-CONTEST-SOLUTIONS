n, t = map(int, input().split())
arr = list(map(int, input().split()))


for i in range(n):
    need=t-arr[i]
    rest=arr[i+1:]
    if need in rest:
        j=rest.index(need)+i+1 # if need  is in the rest of the list , we should determine his position in the original list wich is index in rest +i+1
        print(i+1,j+1) 
        break 
else:
    print(-1,-1)




