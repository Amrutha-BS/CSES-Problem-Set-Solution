n,w=list(map(int,input().split()))
arr=list(map(int,input().split()))
arr.sort()
i=0
j=n-1
count=0
#print(n,w,arr)
while(i<j):
	if arr[i]+arr[j]<=w:
		i+=1
		j-=1
		count+=1
	else:
		j-=1
		count+=1
if i==j:
    count+=1
print(count)