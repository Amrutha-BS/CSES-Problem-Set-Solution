n=int(input())
mod=1000000000+7
dp=[0]*(n+1)
dp[0]=1
for i in range(1,n+1):
    for j in range(1,7):
        if i-j>=0:
            dp[i]=(dp[i]+dp[i-j])%mod
print(dp[n])
'''
n=int(input())
mod=1000000000+7
dp=[0]*(n+6)
dp[0]=1
dp[1]=1
dp[2]=2
dp[3]=4
dp[4]=8
dp[5]=16
for i in range(6,n+1):
    for j in range(1,7):
        dp[i]=(dp[i]+dp[i-j])%mod
print(dp[n])
'''