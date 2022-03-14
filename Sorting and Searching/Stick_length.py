#06-03-2022 N0:2
a=int(input())
arr=list(map(int,input().split()))
arr.sort()
s=0
median=arr[(a-1)//2]
for i in arr:
	s+=abs(i-median)
print(s)