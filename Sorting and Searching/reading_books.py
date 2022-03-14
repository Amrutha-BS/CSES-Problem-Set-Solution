n=int(input())
arr=list(map(int,input().split()))
arr.sort()
s=sum(arr)
if s-arr[n-1]<arr[n-1]:
     print(2*arr[n-1])
else:
     print(s)     