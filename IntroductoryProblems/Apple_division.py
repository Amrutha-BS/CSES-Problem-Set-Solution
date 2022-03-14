n=int(input())
arr=list(map(int,input().split()))
i=0
mini=99999999999
while(i<(1<<n)):
    j=0
    a,b=0,0
    while(j<n):
        if i&(1<<j):
            a+=arr[j]
        else:
            b+=arr[j]  
        j+=1
    mini=min(mini,abs(a-b))
    i+=1  
print(mini)    
    