#import math
n,s=list(map(int,input().split()))
coins=list(map(int,input().split()))
mod=1000000000+7
dp=[0]*(s+1)
dp[0]=1
for i in range(1,s+1):
    for j in coins:
        if i-j>=0:
            dp[i]=(dp[i]+dp[i-j])%mod
print(dp[s])
