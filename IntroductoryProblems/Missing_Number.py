n=int(input())
arr=list(map(int,input().split()))
l=[i for i in range(1,n+1)]
print(sum(l)-sum(arr))