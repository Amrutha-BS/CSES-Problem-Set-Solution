n,x=list(map(int,input().split()))
prices=list(map(int,input().split()))
pages=list(map(int,input().split()))
dp=[0 for i in range(x+1)]
for i in range(1,n+1):
    for pg in range(x,0,-1):
        if prices[i-1]<=pg:
            dp[pg]=max(dp[pg],dp[pg-prices[i-1]]+pages[i-1])
#print(dp)
print(dp[x])
            

