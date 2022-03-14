n=int(input())
arr=list(map(int,input().split()))
s=sum(arr)
dp=[0]*(s+1)
dp[0]=1

for k in range(n):
    for j in range(s,arr[k]-1,-1):
        dp[j]=max(dp[j],dp[j-arr[k]])
            
count=0
for i in range(1,s+1):
    if dp[i]==1:
       count+=1  
print(count)
for i in range(1,s+1):
    if dp[i]==1:
        print(i, end=" ")
       