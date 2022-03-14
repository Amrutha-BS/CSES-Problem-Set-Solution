import math
n,s=list(map(int,input().split()))
coins=list(map(int,input().split()))
dp=[float('inf')]*(s+1)
dp[0]=0
for i in coins:
    for j in range(i,s+1):
        dp[j]=min(dp[j],dp[j-i]+1)
if dp[s]==float('inf'):
    print(-1)
else:
    print(dp[s])
