pairs=[(1,2),(3,4),(5,9),(-1,-6)]
print(min(pairs)) # this will compare the first and the second nummber of each tuples and return the minimum value of both
t=(1,2)<(3,4) # t is True because 1<3 & 2<4


n, t = map(int, input().split())
arr = list(map(int, input().split()))

# intuitio : use a brute force search of all pairs arr[i],arr[j] such as sum==t , then return the mininmum pair 


pairs=[]
for i in range(n):
    for j in range(i+1,n):
        if arr[i]+arr[j]==t:
            pairs.append((i+1,j+1))

# check if there is a valid pair : 
if len(pairs)>0:
    #choose the optimal one with  the smallest (i,j)
    best=min(pairs)
    print((best[0],best[1]))
# if not (-1,-1)
print((-1,-1))


